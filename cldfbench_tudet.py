import pathlib
import subprocess

import conllu
from pytular.util import fetch_sheet
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
        fetch_sheet('languages', output=self.etc_dir / 'languages.csv', delimiter=',')

    def cmd_makecldf(self, args):
        args.writer.cldf.add_component('LanguageTable')
        args.writer.cldf.add_component('ExampleTable', 'conllu')

        for lang in [  # Metalanguages for sentence translations:
            dict(ID='English', Name='English', Glottocode='stan1293'),
            dict(ID='Portuguese', Name='Portuguese', Glottocode='port1283'),
        ]:
            args.writer.objects['LanguageTable'].append(lang)

        langs = {lang['ID']: lang for lang in self.etc_dir.read_csv('languages.csv', dicts=True)}
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
            args.writer.objects['LanguageTable'].append(langs[language])
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
                    ID='{}-{}'.format(langs[language]['ID'], smd['sent_id']),
                    Language_ID=langs[language]['ID'],
                    Primary_Text=smd['text'],
                    Translated_Text=translation[1],
                    Meta_Language_ID=translation[0],
                    conllu=sentence.serialize(),
                ))
