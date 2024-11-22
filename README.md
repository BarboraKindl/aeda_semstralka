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
pip install python-dotenv pandas 
```


### Docs


 excel_to_csv

> This script converts Excel files (.xlsx) into CSV files (.csv). It uses the Pandas library for handling data conversion and supports flexible configuration using a .env file for input and output file paths.

### liks

- [článek od Šonky](https://www.neurologiepropraxi.cz/pdfs/neu/2008/05/07.pdf)
