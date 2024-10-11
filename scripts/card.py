import sqlite3
import typst
from pathlib import Path

def get_database(db_path):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    return cursor

def get_goals_by_cycle(db, cycle_code_list):
    sql="SELECT * FROM lp21 WHERE cycle_code in ({seq})".format(seq=','.join(['?']*len(cycle_code_list)))
    db.execute(sql, cycle_code_list)
    rows = db.fetchall()
    print(f'Searching for goals in {cycle_code_list}')
    print(f'Found {len(rows)} goals')
    return rows

def create_typst_document(rows, typst_template_file='./template/card.typ', target_file='./build/card-set.typ'):
    file = open(typst_template_file, 'r', encoding='utf-8')
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
        #print(f'{row['level_code']} Text Length {text_length} on {nofLines} Lines')

    # Put it all into a typst file and compile it
    Path(target_file).resolve().parent.mkdir(exist_ok=True)
    with open(target_file, 'w', encoding='utf-8') as card_set:
        card_set.write(card)


pdf_list = [
    { "name": "Karteikarten Kindergarten", "cycle": ["1"] },
    { "name": "Karteikarten 1-2. Klasse Grundanforderungen", "cycle": ["1b"] },
    { "name": "Karteikarten 1-2. Klasse Optional", "cycle": ["1,2a", "1,2", "1b,2a"] },
    { "name": "Karteikarten 3-4. Klasse Grundanforderungen", "cycle": ["2a", ] },
    { "name": "Karteikarten 3-4. Klasse Optional", "cycle": ["2", "2,3", "2,3a"] },
    { "name": "Karteikarten 5-6. Klasse Grundanforderungen", "cycle": ["2b", ] },
    { "name": "Karteikarten 5-6. Klasse Optional", "cycle": ["2b,3", "2b,3a", "2b,3ao"] },
    { "name": "Karteikarten 7-8. Klasse Grundanforderungen", "cycle": ["3a", ] },
    { "name": "Karteikarten 7-8. Klasse Optional", "cycle": ["3", "3o", "3ao"] },
    { "name": "Karteikarten 9. Klasse Grundanforderungen", "cycle": ["3b", ] },
    { "name": "Karteikarten 9. Klasse Optional", "cycle": ["3bo"] }
]

if __name__ == '__main__':
    
    db = get_database('./content/sqlite/lp21.db')

    for document in pdf_list:
        name = document['name']
        print(f'Creating document "{name}.pdf"')
        goals = get_goals_by_cycle(db, document['cycle'])
        create_typst_document(goals, typst_template_file='./template/card.typ', target_file='./build/' + name + '.typ' )
        typst.compile("./build/card-set.typ", output="./content/pdf/" + name + '.pdf')
        print("")
