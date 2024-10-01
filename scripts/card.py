import sqlite3
import typst

# Connect to SQLite database
db_name = 'lp21.db'
conn = sqlite3.connect(db_name)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


cursor.execute('SELECT * FROM lp21 WHERE cycle_code="1"')

rows = cursor.fetchall()
print(f'Found {len(rows)} goals')

row = rows[0]

print(dict(row))
typst_card=f'#card(category: "{row['competence_title']}", code: "{row['level_code']}", class: "{row['cycle_name']}", ladder: "{row['cycle_ladder']}", color: "{row['subject_color']}",  optional: {row['cycle_optional']}, )[{row['level_text']}]'

print(typst_card)


file_name = './scripts/card.typ'
file = open(file_name, 'r', encoding='utf-8')
card = file.read()

for row in rows:

    preamble = "Die Schülerinnen und Schüler "
    lines =  row['level_text'].split('\r\n')
    text = ""
    for line in lines[0:-1]:
        text = text + preamble + line + "\r\n" 
    typst_card=f'#card(category: "{row['competence_title']}", code: "{row['level_code']}", class: "{row['cycle_name']}", ladder: "{row['cycle_ladder']}", color: "{row['subject_color']}",  optional: {row['cycle_optional']}, )[{text}]\r\n'
    card += typst_card

with open('card-set.typ', 'w', encoding='utf-8') as card_set:
    card_set.write(card)
    typst.compile("card-set.typ", output="card-set2.pdf")