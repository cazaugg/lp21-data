import sqlite3
import json

# Connect to SQLite database
db_name = 'lp21.db'
conn = sqlite3.connect(db_name)
cursor = conn.cursor()


#cursor.execute('DROP VIEW lp21')

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
conn.close()
