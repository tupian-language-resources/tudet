import re
import shutil
import pathlib

import conllu
import git
from cldfbench import Dataset as BaseDataset

TRANSLATIONS = {
    'eng': 'English',
    'port': 'Portuguese',
    'portuguese': 'Portuguese'
}


def update_fork(p):
    r = git.Repo(str(p))
    r.git.checkout('origin/dev')
    for remote in r.remotes:
        if remote.name == 'upstream':
            break
    else:
        raise ValueError('no remote called upstream')
    remote.fetch()
    r.git.merge('upstream/dev')


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "tudet"

    def cldf_specs(self):  # A dataset must declare all CLDF sets it creates.
        return super().cldf_specs()

    def cmd_download(self, args):
        """
        Collect the data from the dev branches of the UD repository forks
        """
        prefix, suffix = 'UD_', '-TuDeT'
        for d in self.dir.resolve().parent.glob('{}*{}'.format(prefix, suffix)):
            if d.is_dir():
                update_fork(d)
                lang = d.name.replace(prefix, '').replace(suffix, '')
                out = self.raw_dir / lang
                if not out.exists():
                    out.mkdir()
                for p in d.glob('*.conllu'):
                    shutil.copy(str(p), out / p.name)

    def cmd_makecldf(self, args):
        args.writer.cldf.add_component('ExampleTable', 'conllu')
        for p in self.raw_dir.glob('*/*.conllu'):
            try:
                sentences = conllu.parse(p.read_text(encoding='utf8'))
            except:
                print(p.resolve())
                t = p.read_text(encoding='utf8')
                for i, chunk in enumerate(t.split('# sent_id')):
                    if i:
                        try:
                            conllu.parse('# sent_id' + chunk)
                        except:
                            print('# sent_id' + chunk)
                            raise
                raise
            for sentence in sentences:
                smd = {k.lower(): v for k, v in sentence.metadata.items()}
                if not ('sent_id' in smd and 'text' in smd and any('text_' + code in smd for code in TRANSLATIONS)):
                    print(p, smd)
                    continue

                for code, lang in TRANSLATIONS.items():
                    if 'text_' + code in smd:
                        translation = lang, smd['text_' + code]
                        break
                else:
                    raise ValueError()

                args.writer.objects['ExampleTable'].append(dict(
                    ID='{}-{}'.format(p.parent.name, smd['sent_id']),
                    Language_ID=p.parent.name,
                    Primary_Text=smd['text'],
                    Translated_Text=translation[1],
                    Meta_Language_ID=translation[0],
                    conllu=sentence.serialize(),
                ))
