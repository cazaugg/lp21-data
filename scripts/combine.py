import json
import os, json

path_to_json = 'subjects'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json') and pos_json.startswith('Ziele-')]
print(json_files)  # for me this prints ['foo.json']

combined_content = []

for file_path in json_files:
    file_path = os.path.join(path_to_json, file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        new = json.load(file)
        combined_content = combined_content + new
        print(f'Opened file {file.name} containing {len(new)} goals')

with open('./subjects/LP21.json', 'w', encoding='utf-8') as outfile:
    outfile.write(json.dumps(combined_content, ensure_ascii=False, indent=4))
    print(f'Written all goals to {outfile.name}')