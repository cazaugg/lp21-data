import sqlite3
import typst

# Connect to SQLite database
db_name = 'lp21.db'
conn = sqlite3.connect(db_name)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


cursor.execute('SELECT * FROM lp21 WHERE cycle_code in ("1", "1b", "1,2a", "1,2", "1b,2", "1b,2a")')

rows = cursor.fetchall()
print(f'Found {len(rows)} goals')

file_name = './scripts/card.typ'
file = open(file_name, 'r', encoding='utf-8')
card = file.read()

for row in rows:

    # We need to split the competence title into two rows as some are very long
    competence = "\n".join(row['competence_title'].rsplit(".", 1))
    competence = competence.replace(".", ": ")

    # We need to add the preamble to every line 
    preamble = "Die Schülerinnen und Schüler "
    text_length = len(row['level_text'])
    lines =  row['level_text'].split('\n')
    nofLines = len(lines) - 1
    
    # Parse code (so we can append page index if needed)
    code = row['level_code']

    # If the goal has more than 3 lines, we put the first two on another page
    text = ""    
    if nofLines >= 4 or (text_length > 410 and nofLines == 3 ):
        text = text + preamble + lines[0] + "\n" 
        text = text + preamble + lines[1] + "\n"    
        typst_card=f'#card(category: "{competence}", code: "{code} | 1/2", class: "{row['cycle_name']}", ladder: "{row['cycle_ladder']}", color: "{row['subject_color']}",  optional: {row['cycle_optional']}, )[{text}]\r\n'
        card += typst_card
        lines = lines[2:]
        code += " | 2/2"
    
    # Assemble a single card normally
    text = ""
    for line in lines[0:-1]:
        text = text + preamble + line + "\n" 

    # Assmeble the typst function call for a card
    typst_card=f'#card(category: "{competence}", code: "{code}", class: "{row['cycle_name']}", ladder: "{row['cycle_ladder']}", color: "{row['subject_color']}",  optional: {row['cycle_optional']}, )[{text}]\r\n'
    card += typst_card
    print(f'{row['level_code']} Text Length {text_length} on {nofLines} Lines')

# Put it all into a typst file and compile it
with open('card-set.typ', 'w', encoding='utf-8') as card_set:
    card_set.write(card)
    typst.compile("card-set.typ", output="card-set.pdf")