<a name="ds-genericmetadatajson"> </a>

# Generic TuDeT: Tupían Dependency Treebank

**CLDF Metadata**: [Generic-metadata.json](./Generic-metadata.json)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF Generic](http://cldf.clld.org/v1.0/terms.rdf#Generic)
[dc:identifier](http://purl.org/dc/terms/identifier) | https://tular.clld.org/contributions/tudet
[dc:license](http://purl.org/dc/terms/license) | https://creativecommons.org/licenses/by-sa/4.0/
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | https://github.com/tupian-language-resources/tudet
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="https://github.com/tupian-language-resources/tudet/tree/dd64b42">tupian-language-resources/tudet v0.3-1-gdd64b42</a></li><li><a href="https://github.com/glottolog/glottolog/tree/v4.5">Glottolog v4.5</a></li><li><a href="https://github.com/UniversalDependencies/UD_Teko-TuDeT/tree/23674b7">UniversalDependencies/UD_Teko-TuDeT r2.10-9-g23674b7</a></li><li><a href="https://github.com/UniversalDependencies/UD_Makurap-TuDeT/tree/r2.10">UniversalDependencies/UD_Makurap-TuDeT r2.10</a></li><li><a href="https://github.com/UniversalDependencies/UD_Kaapor-TuDeT/tree/r2.10">UniversalDependencies/UD_Kaapor-TuDeT r2.10</a></li><li><a href="https://github.com/UniversalDependencies/UD_Guajajara-TuDeT/tree/r2.10">UniversalDependencies/UD_Guajajara-TuDeT r2.10</a></li><li><a href="https://github.com/UniversalDependencies/UD_Akuntsu-TuDeT/tree/r2.10">UniversalDependencies/UD_Akuntsu-TuDeT r2.10</a></li><li><a href="https://github.com/UniversalDependencies/UD_Munduruku-TuDeT/tree/29a9aa1">UniversalDependencies/UD_Munduruku-TuDeT r2.10-2-g29a9aa1</a></li><li><a href="https://github.com/UniversalDependencies/UD_Karo-TuDeT/tree/r2.10">UniversalDependencies/UD_Karo-TuDeT r2.10</a></li><li><a href="https://github.com/UniversalDependencies/UD_Tupinamba-TuDeT/tree/4e82687">UniversalDependencies/UD_Tupinamba-TuDeT r2.10-3-g4e82687</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>python</strong>: 3.8.10</li><li><strong>python-packages</strong>: <a href="./requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | tudet
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-languagescsv"></a>Table [languages.csv](./languages.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable)
[dc:extent](http://purl.org/dc/terms/extent) | 11


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal` | 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal` | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string` | 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string` | 

## <a name="table-examplescsv"></a>Table [examples.csv](./examples.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ExampleTable](http://cldf.clld.org/v1.0/terms.rdf#ExampleTable)
[dc:extent](http://purl.org/dc/terms/extent) | 2961


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Primary_Text](http://cldf.clld.org/v1.0/terms.rdf#primaryText) | `string` | The example text in the source language.
[Analyzed_Word](http://cldf.clld.org/v1.0/terms.rdf#analyzedWord) | list of `string` (separated by `\t`) | The sequence of words of the primary text to be aligned with glosses
[Gloss](http://cldf.clld.org/v1.0/terms.rdf#gloss) | list of `string` (separated by `\t`) | The sequence of glosses aligned with the words of the primary text
[Translated_Text](http://cldf.clld.org/v1.0/terms.rdf#translatedText) | `string` | The translation of the example text in a meta language
[Meta_Language_ID](http://cldf.clld.org/v1.0/terms.rdf#metaLanguageReference) | `string` | References the language of the translated text<br>References [languages.csv::ID](#table-languagescsv)
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
`conllu` | `string` | 
[Contribution_ID](http://cldf.clld.org/v1.0/terms.rdf#contributionReference) | `string` | References [contributions.csv::ID](#table-contributionscsv)

## <a name="table-contributionscsv"></a>Table [contributions.csv](./contributions.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ContributionTable](http://cldf.clld.org/v1.0/terms.rdf#ContributionTable)
[dc:extent](http://purl.org/dc/terms/extent) | 8


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[Contributor](http://cldf.clld.org/v1.0/terms.rdf#contributor) | `string` | 
[Citation](http://cldf.clld.org/v1.0/terms.rdf#citation) | `string` | 

