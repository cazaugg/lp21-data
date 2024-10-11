import re
import pandas as pd
import sqlite3

db_file = './content/sqlite/lp21.db'
conn = sqlite3.connect(db_file, isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)
cursor = conn.cursor()

cursor.execute("SELECT cycle_name, cycle_code, count(cycle_code), cycle_optional FROM lp21 GROUP by cycle_code ORDER by cycle_ladder")

text = """
Zusammenfassung Lehrplan 21 nach Klassen:

| Jahr | Anzahl Ziele | Optional | Zyklus Code |
| ---- | ------------ | -------- | ----------- |
"""
for row in cursor.fetchall():
    if row[3] == 1:
        optional = "ja"
    else:
        optional = "neine"
    text += (f'| {row[0]} | {row[2]} | {optional} | {row[1]} |\r\n')

print(text)



