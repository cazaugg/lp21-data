import sqlite3
import json
import os

# Connect to SQLite database
db_name = './content/sqlite/lp21.db'
if os.path.exists(db_name): os.remove(db_name)
conn = sqlite3.connect(db_name)
cursor = conn.cursor()
print(f'Created Datase {db_name}')

###############################################################################
# Create Database for Competence Levels
###############################################################################

file_name = './content/json/goals.json'
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

file_name = './content/json/competences.json'
file = open(file_name, 'r', encoding='utf-8')
content = json.load(file)

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

file_name = './content/json/subjects.json'
file = open(file_name, 'r', encoding='utf-8')
subjects = json.load(file)

print(f'Opened file {file_name}')
print(f'It contains {len(subjects)} objects')

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
file_name = './content/json/cycles.json'
file = open(file_name, 'r', encoding='utf-8')
cycles = json.load(file)

print(f'Opened file {file_name}')
print(f'It contains {len(cycles)} objects')

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