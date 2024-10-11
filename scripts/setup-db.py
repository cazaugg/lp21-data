import sqlite3
import json

# Connect to SQLite database
db_name = 'lp21.db'
conn = sqlite3.connect(db_name)
cursor = conn.cursor()
print(f'Created Datase {db_name}')

###############################################################################
# Create Database for Competence Levels
###############################################################################

file_name = './subjects/LP21.json'
file = open(file_name, 'r', encoding='utf-8')
content = json.load(file)

print(f'Opened file {file_name}')
print(f'It contains {len(content)} objects')

# Create table (if it doesn't exist)
#cursor.execute("DROP TABLE levels")
create_table_sql = '''
CREATE TABLE IF NOT EXISTS levels (
    subject TEXT,
    competence TEXT,
    code TEXT,
    cycle TEXT,
    text TEXT
)
'''
cursor.execute(create_table_sql)

insert_sql = '''
INSERT INTO levels (subject, competence, code, cycle, text)
VALUES (?, ?, ?, ?, ?)
'''
for goal in content:
    locals().update(goal)
    path = Code.split('.')
    Subject = path[0]
    Competence = '.'.join(path[0:-1])
    lines = ""    
    for line in goal['Text']:
        lines = lines + line + '\r\n'
    cursor.execute(insert_sql, (Subject, Competence, Code, Zyklus, lines))
conn.commit()

###############################################################################
# Create Database for Competences
###############################################################################

file_name = './subjects/Kompetenzen.json'
file = open(file_name, 'r', encoding='utf-8')
content = json.load(file)

seen = set()
dupes = []

for comp in content:
    code = comp['Code']
    if code in seen:
        dupes.append(code)
    else:
        seen.add(code)

print(f"Dublicates {dupes}")


print(f'Opened file {file_name}')
print(f'It contains {len(content)} objects')

# Create table (if it doesn't exist)
#cursor.execute("DROP TABLE levels")
create_table_sql = '''
CREATE TABLE IF NOT EXISTS competences (
    code TEXT,
    title TEXT,
    text TEXT,
    PRIMARY KEY (code)
)
'''
cursor.execute(create_table_sql)

insert_sql = '''
INSERT INTO competences (code, title, text)
VALUES (?, ?, ?)
'''
for goal in content:
    locals().update(goal)
    cursor.execute(insert_sql, (Code, Title, Text))
conn.commit()

###############################################################################
# Create Database for Subjects
###############################################################################

create_cycles = '''
CREATE TABLE IF NOT EXISTS subjects (
    name TEXT NOT NULL,
    nick TEXT NOT NULL,
    code TEXT NOT NULL,
    color TEXT,
    PRIMARY KEY (code)
)
'''
cursor.execute(create_cycles)

subjects = [
    { "Name": "Deutsch",                            "Nick": "Deutsch",    "Code": "D",   "Color": "#fccdcc"  },
    { "Name": "Mathematik",                         "Nick": "Math",       "Code": "MA",  "Color": "#cfe4ff"  },
    { "Name": "Medien und Informatik",              "Nick": "Informatik", "Code": "MI",  "Color": "#cfffe6"  },
    { "Name": "Musik",                              "Nick": "Musik",      "Code": "MU",  "Color": "#d0ffff"  },
    { "Name": "Natur, Mensch, Gesellschaft",        "Nick": "NMG",        "Code": "NMG", "Color": "#ceffcc"  },
    { "Name": "Bewegung und Sport",                 "Nick": "Sport",      "Code": "BS",  "Color": "#fdffcc"  },
    { "Name": "Textiles und Technisches Gestalten", "Nick": "Werken",     "Code": "TTG", "Color": "#cec9ff"  },
    { "Name": "Bildnerisches Gestalten",            "Nick": "Zeichnen",   "Code": "BG",  "Color": "#fce7cc"  },
]

sql = '''
INSERT INTO subjects (name, nick, code, color)
VALUES (?, ?, ?, ?)
'''

for subject in subjects:
    locals().update(subject)
    cursor.execute(sql, (Name, Nick, Code, Color))

conn.commit()


###############################################################################
# Create Database for Cycles
###############################################################################

create_cycles = '''
CREATE TABLE IF NOT EXISTS cycles (
    code TEXT NOT NULL,
    name TEXT NOT NULL,
    ladder TEXT NOT NULL,
    optional INTEGER,
    PRIMARY KEY (code)
)
'''
cursor.execute(create_cycles)

cycles = [
    { 'Code': '1',      'Name': 'Kindergarten - 2. Klasse', 'Optional': False, 'Ladder': '12'},
    { 'Code': '1,2',    'Name': 'Kindergarten - 6. Klasse', 'Optional': False, 'Ladder': '1234'},
    { 'Code': '1,2a',   'Name': 'Kindergarten - 4. Klasse', 'Optional': False, 'Ladder': '123'},
    { 'Code': '1b',     'Name': '1. - 2. Klasse',           'Optional': False, 'Ladder': '2'},
    { 'Code': '1b,2a',  'Name': '1. - 4. Klasse',           'Optional': False, 'Ladder': '23'},
    { 'Code': '2',      'Name': '3. - 6. Klasse',           'Optional': False, 'Ladder': '34'},
    { 'Code': '2,3',    'Name': '3. - 9. Klasse',           'Optional': False, 'Ladder': '3456'},
    { 'Code': '2,3a',   'Name': '3. - 8. Klasse',           'Optional': False, 'Ladder': '345'},
    { 'Code': '2a',     'Name': '3. - 4. Klasse',           'Optional': False, 'Ladder': '3'},
    { 'Code': '2b',     'Name': '5. - 6. Klasse',           'Optional': False, 'Ladder': '4'},
    { 'Code': '2b,3',   'Name': '5. - 9. Klasse',           'Optional': False, 'Ladder': '456'},
    { 'Code': '2b,3a',  'Name': '5. - 8. Klasse',           'Optional': False, 'Ladder': '45'},
    { 'Code': '2b,3ao', 'Name': '5. - 8. Klasse',           'Optional': True , 'Ladder': '45'},
    { 'Code': '3',      'Name': '7. - 9. Klasse',           'Optional': False, 'Ladder': '56'},
    { 'Code': '3a',     'Name': '7. - 8. Klasse',           'Optional': False, 'Ladder': '5'},
    { 'Code': '3ao',    'Name': '7. - 8. Klasse',           'Optional': True , 'Ladder': '5'},
    { 'Code': '3b',     'Name': '9. Klasse',                'Optional': False, 'Ladder': '6'},
    { 'Code': '3bo',    'Name': '9. Klasse',                'Optional': True , 'Ladder': '6'},
    { 'Code': '3o',     'Name': '7. - 9. Klasse',           'Optional': True , 'Ladder': '56'}
]

sql = '''
INSERT INTO cycles (code, name, ladder, optional)
VALUES (?, ?, ?, ?)
'''

for cycle in cycles:
    locals().update(cycle)
    cursor.execute(sql, (Code, Name, Ladder, Optional))

conn.commit()

###############################################################################
# Create View
###############################################################################

sql='''
CREATE VIEW lp21 AS
SELECT levels.code as level_code, levels.text as level_text, 
subject as subject_code, subjects.name as subject_name, subjects.nick as subject_nick, subjects.color as subject_color, 
competence as comptetence_code, competences.title as competence_title, competences.text as competence_text,
cycle as cycle_code, cycles.name as cycle_name, cycles.ladder as cycle_ladder, cycles.optional as cycle_optional
FROM levels
INNER JOIN subjects ON levels.subject=subjects.code
INNER JOIN competences ON levels.competence=competences.code
INNER JOIN cycles ON levels.cycle=cycles.code
'''

cursor.execute(sql)
conn.commit()

# Close the connection
conn.close()
print("Data inserted successfully.")