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
 
- [škála UDPRS III -  Unified Parkinson‘s disease rating scale](https://www.neurologiepropraxi.cz/pdfs/neu/2011/92/07.pdf)
  - nemotorické vlivy Pakinsonovy nemoci na pacientovy aktivity denního života
  - 13 otázek
  -  Part I: Mentation, Behavior, Mood
  - Part II: Activities of Daily Living (Determine for “on” or “off”, indicating either a “good” or “bad” day, respectively.)
  - Part III: Motor Examination
  - Part IV: Complications of Therapy (in the past week)
  - Part V: H&Y staging scale
  - Part VI: S&E ADL scale

- [z PUBMED - Rapid Eye Movement Sleep Behavior Disorder](https://www.ncbi.nlm.nih.gov/books/NBK555928/)
   - RBD zahrnuje chování spojené se sny, kdy dochází k ztrátě svalové atonie během REM spánku, což může způsobit zranění pacientům i jejich partnerům.
   - Silně spojené s neurodegenerativními alfa-synukleinopatiemi, jako je Parkinsonova choroba a demence s Lewyho těly.
   - Příznaky mohou předcházet neurodegenerativní onemocnění i o desítky let.
   - Diagnóza vyžaduje polysomnografii, léčba zahrnuje prevenci zranění a léky jako melatonin nebo klonazepam.
   - Faktory rizika: Věk, pohlaví (častější u mužů), užívání antidepresiv, narkolepsie a neurologická onemocnění.
   - Typy RBD:
     Idiopatické: Nejčastější u neurodegenerativních synukleinopatií.
     Léky indukované: Nejvíce spojené s antidepresivy (SSRIs, TCA, MAOIs) a alkoholem.
     Sekundární: Spojeno s nemocemi jako narkolepsie nebo traumata.
   - RBD spojené s narkolepsií má jiný průběh a méně násilné chování.
   - Prevalence: ~0,5 % v běžné populaci, u starších lidí 5-13 %.
   - Častější u mužů, ale u lidí do 50 let rovnoměrné rozdělení pohlaví.
   - Silná souvislost s psychiatrickými poruchami a užíváním antidepresiv.
   - Ztráta atonie během REM spánku kvůli dysfunkci mozkového kmene.
Silná spojitost s neurodegenerativními synukleinopatiemi, přičemž po 12 letech se 74 % pacientů vyvine v tato onemocnění.
   - Související poruchy zahrnují progresivní supranukleární paralýzu a frontotemporální demenci.

  
- [RBD and Neurodegenerative Diseases](https://link.springer.com/article/10.1007/s12035-016-9831-4)
    - U 18–52 % pacientů s Parkinsonovou chorobou se RBD vyvine před nástupem Parkinsonovy choroby, u ostatních současně nebo později.
    - RBD je častější u pacientů s akineticko-rigidní formou PD, ale ve větších studiích nebyl nalezen preferovaný podtyp.
    - Pacienti s PD a RBD mají obvykle delší trvání nemoci, více pádů, psychiatrické komorbidity a vyšší dávky levodopy.
    - RBD je spojeno s více REM spánkem, periodickými pohyby nohou, vyššími změnami systolického krevního tlaku a horší kognicí.
    - RBD a REM spánek bez atonie (RWA) jsou spojeny s rychlejším motorickým zhoršením u PD, což naznačuje, že porucha svalové atonie může být ukazatelem rychlejšího progrese nemoci.

  
- [Abnormal eye movements in Parkinson's disease: From experimental study to clinical application](https://www.sciencedirect.com/science/article/pii/S1353802023008702)


- [Monitoring Eye Movement in Patients with Parkinson’s Disease: What Can It Tell Us?](https://www.dovepress.com/monitoring-eye-movement-in-patients-with-parkinsons-disease-what-can-i-peer-reviewed-fulltext-article-EB)

  


### random 

Pro zdravého člověka je sen pouhou duševní aktivitou. Spící člověk se může ve snu procházet, ale jeho tělo zůstává nehybné, atonické. U pacientů s poruchou chování v REM spánku (Rapid Eye Movement Sleep Behaviour Disorder, zkratka RBD) však k atonii během snění nedochází a pacienti své sny prožívají i tělesným pohybem, který koresponduje s jejich snovou aktivitou. Mnozí ze spaní mluví, křičí, kopou, jsou náměsíční a trpí tím nejen oni sami, ale i jejich partneři. Pacienti s RBD jsou navíc ve velkém riziku (více než 80% konvertujících pacientů) rozvinutí Parkinsonovy nemoci (viz Postuma et al. 2012, Schenck et al. 2013). U značné části pacientů s RBD lze tedy pozorovat proces neurodegenerace v raném stádiu ještě před rozvinutím typických klinických příznaků PD.

- jak jako se tam měří oči?
- jak pozorujeme v ranem stanem stadiu?
