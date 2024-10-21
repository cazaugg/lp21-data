import pandas as pd
import sqlite3
import csv

tables_list = ['lp21', 'subjects', 'competences', 'goals', 'cycles']

db_file = './content/sqlite/lp21.db'
conn = sqlite3.connect(db_file, isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)

for table in tables_list:
    db_df = pd.read_sql_query("SELECT * FROM " + table, conn)
    db_df.to_csv('./content/csv/' + table + '.csv', index=False, quoting=csv.QUOTE_ALL)
    print(f'Create "{table}.csv"')

for table in tables_list:
    db_df = pd.read_sql_query("SELECT * FROM " + table, conn)
    db_df = db_df.replace('\u2248', '~', regex = True)
    db_df = db_df.replace('\u2260', '!=', regex = True)
    db_df = db_df.replace('\u221a', 'sqrt', regex = True)
    db_df = db_df.replace('\u2264', '<=', regex = True)
    db_df = db_df.replace('\u2265', '>=', regex = True)
    db_df = db_df.replace('\u2078', '^8', regex = True)
    db_df = db_df.replace('\u2192', '->', regex = True)
    db_df = db_df.replace('\u2155', '1/5', regex = True)
    db_df = db_df.replace('\u2074', '^4', regex = True)
    db_df = db_df.replace('\u215c', '3/8', regex = True)
    db_df = db_df.replace('\u215d', '5/8', regex = True)
    db_df = db_df.replace('\u2153', '1/3', regex = True)
    db_df = db_df.replace('\u22c5', '*', regex = True)
    db_df = db_df.replace('\u2076', '^6', regex = True)
    db_df = db_df.replace('\u02d9', '°', regex = True)
    db_df = db_df.replace('\u215b', '1/8', regex = True)
    db_df = db_df.replace('\u2157', '3/5', regex = True)
    if 'text' in db_df:
        db_df['text'] = db_df['text'].str.rstrip()
        db_df['text'] = db_df['text'].str.replace('\r\n','"')

    db_df.to_csv('./content/csv-excel/' + table + '.csv', index = False, quoting=csv.QUOTE_ALL, encoding='cp1252')
    print(f'Create "{table}.csv"')

