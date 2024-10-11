import pandas as pd
import sqlite3

tables_list = ['lp21', 'subjects', 'competences', 'goals', 'cycles']

db_file = './content/sqlite/lp21.db'
conn = sqlite3.connect(db_file, isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)

for table in tables_list:
    db_df = pd.read_sql_query("SELECT * FROM " + table, conn)
    db_df.to_csv('./content/csv/' + table + '.csv', index=False)
    print(f'Create "{table}.csv"')
