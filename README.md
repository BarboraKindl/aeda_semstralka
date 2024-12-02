# Pohyby očí a porucha chování v REM spánku

### set-up
```bash
touch .gitignore
touch .env
```
- into .gitignore write this
>.venv
> 
> .env

- into .env write this 
> INPUT_FILE=data.xlsx
> 
> OUTPUT_FILE=data.csv

- create your own env for python and active it
```bash
python3 -m venv .venv
source .venv/bin/activate
```
- install packages
```bash
pip install python-dotenv pandas openpyxl
```

### Docs

 excel_to_csv

> This script converts Excel files (.xlsx) into CSV files (.csv). It uses the Pandas library for handling data conversion and supports flexible configuration using a .env file for input and output file paths.

### links

- [článek od Šonky](https://www.neurologiepropraxi.cz/pdfs/neu/2008/05/07.pdf)
  - PLMS – periodické pohyby končetinami ve spánku (periodic limb movements in sleep)
  - PSG – polysomnografie
  - RBD – porucha chování v REM spánku (REM sleep
  - behavior disorder
  - Lewyho tělíska - abnormální bílkovinné usazeniny uvnitř nervových buněk, které se vyskytují zejména u pacientů s demencí s Lewyho tělísky a s parkinsonskými syndromy. Viz také demence s Lewyho tělísky.
  - atonie svalů = absence svalového napětí
  - musculi cricoarythenoidales posteriores - Jako jediný ze svalů hrtanu rozevírá hlasivkovou štěrbinu a udržuje ji při dýchání otevřenou v respiračním postavení. Při porušení jeho inervace (riziko při operacích štítné žlázy) hrozí udušení. Pokud se nepodaří inervaci obnovit, je třeba provést laterofixaci nebo resekci hlasivky. Jeho snopce směrem k úponu konvergují. [zdroj](https://www.wikiskripta.eu/w/Svaly_laryngu)
 
    
- [z PUBMED - Rapid Eye Movement Sleep Behavior Disorder](https://www.ncbi.nlm.nih.gov/books/NBK555928/)
   - RBD zahrnuje chování spojené se sny, kdy dochází k ztrátě svalové atonie během REM spánku, což může způsobit zranění pacientům i jejich partnerům.
   - Silně spojené s neurodegenerativními alfa-synukleinopatiemi, jako je Parkinsonova choroba a demence s Lewyho těly.
Příznaky mohou předcházet neurodegenerativní onemocnění i o desítky let.
Diagnóza vyžaduje polysomnografii, léčba zahrnuje prevenci zranění a léky jako melatonin nebo klonazepam.
Příčiny

Faktory rizika: Věk, pohlaví (častější u mužů), užívání antidepresiv, narkolepsie a neurologická onemocnění.
Typy RBD:
Idiopatické: Nejčastější u neurodegenerativních synukleinopatií.
Léky indukované: Nejvíce spojené s antidepresivy (SSRIs, TCA, MAOIs) a alkoholem.
Sekundární: Spojeno s nemocemi jako narkolepsie nebo traumata.
RBD spojené s narkolepsií má jiný průběh a méně násilné chování.
Epidemiologie

Prevalence: ~0,5 % v běžné populaci, u starších lidí 5-13 %.
Častější u mužů, ale u lidí do 50 let rovnoměrné rozdělení pohlaví.
Silná souvislost s psychiatrickými poruchami a užíváním antidepresiv.
U 30 % mladých lidí s narkolepsií typu I.
Patofyziologie

Ztráta atonie během REM spánku kvůli dysfunkci mozkového kmene.
Silná spojitost s neurodegenerativními synukleinopatiemi, přičemž po 12 letech se 74 % pacientů vyvine v tato onemocnění.
Související poruchy zahrnují progresivní supranukleární paralýzu a frontotemporální demenci.
Nové spojení s protilátkami (anti-IgLON5), které naznačuje tauopatii.
Závěr

RBD může odhalit základní neurodegenerativní nebo imunitně zprostředkované nemoci, přičemž serotonergní léky mohou příznaky zhoršit.

  
- [RBD and Neurodegenerative Diseases](https://link.springer.com/article/10.1007/s12035-016-9831-4)

  
- [REM sleep behavior disorder (RBD)](https://sci-hub.se/https://doi.org/10.1016/j.nbd.2020.104996)

  


### random 

Pro zdravého člověka je sen pouhou duševní aktivitou. Spící člověk se může ve snu procházet, ale jeho tělo zůstává nehybné, atonické. U pacientů s poruchou chování v REM spánku (Rapid Eye Movement Sleep Behaviour Disorder, zkratka RBD) však k atonii během snění nedochází a pacienti své sny prožívají i tělesným pohybem, který koresponduje s jejich snovou aktivitou. Mnozí ze spaní mluví, křičí, kopou, jsou náměsíční a trpí tím nejen oni sami, ale i jejich partneři. Pacienti s RBD jsou navíc ve velkém riziku (více než 80% konvertujících pacientů) rozvinutí Parkinsonovy nemoci (viz Postuma et al. 2012, Schenck et al. 2013). U značné části pacientů s RBD lze tedy pozorovat proces neurodegenerace v raném stádiu ještě před rozvinutím typických klinických příznaků PD.

- jak jako se tam měří oči?
- jak pozorujeme v ranem stanem stadiu?
