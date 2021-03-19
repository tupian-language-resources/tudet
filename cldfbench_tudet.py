import pathlib
import subprocess

import conllu
from cldfbench import Dataset as BaseDataset

TRANSLATIONS = {
    'eng': 'English',
    'port': 'Portuguese',
    'portuguese': 'Portuguese'
}


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "tudet"

    def cldf_specs(self):  # A dataset must declare all CLDF sets it creates.
        return super().cldf_specs()

    def iter_conllu(self):
        prefix, suffix = 'UD_', '-TuDeT'
        for d in sorted(self.raw_dir.glob('{}*{}'.format(prefix, suffix)), key=lambda p: p.name):
            lang = d.name.replace(prefix, '').replace(suffix, '')
            for path in sorted(d.glob('*.conllu'), key=lambda p: p.name):
                yield lang, path

    def cmd_download(self, args):
        """
        Collect the data from the dev branches of the UD repository forks
        """
        subprocess.check_call(
            'git -C {} submodule update --remote'.format(self.dir.resolve()), shell=True)

    def cmd_makecldf(self, args):
        args.writer.cldf.add_component('ExampleTable', 'conllu')
        for language, p in self.iter_conllu():
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
                    ID='{}-{}'.format(language, smd['sent_id']),
                    Language_ID=language,
                    Primary_Text=smd['text'],
                    Translated_Text=translation[1],
                    Meta_Language_ID=translation[0],
                    conllu=sentence.serialize(),
                ))
