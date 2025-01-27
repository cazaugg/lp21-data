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


cursor.execute("SELECT code from cycles")
cycles = cursor.fetchall()

cursor.execute("SELECT code from subjects")
subjects = cursor.fetchall()

text = "| Fach \ Zyklus |"
for cycle in cycles:
    text += " " + cycle[0] + " |"
print(text)
print( "| --- |" + " --- |" * len(cycles))

for subject in subjects:
    text = "| " + subject[0] + " |"
    for cycle in cycles:
        cursor.execute('SELECT level_code, count(level_code), subject_code, cycle_code from LP21 where subject_code=? and cycle_code=?', [subject[0], cycle[0]])
        for row in cursor.fetchall():
            text += f' {row[1]} |'
    print(text)


text = "| Total |"
for cycle in cycles:
    cursor.execute('SELECT level_code, count(level_code), subject_code, cycle_code from LP21 where cycle_code=?', [cycle[0]])
    for row in cursor.fetchall():
        text += f' {row[1]} |'
print(text)