import json
note = input('Введите заметку: \n')
with open('notes.json', 'r') as f:
    json.dump(note, f, ensure_ascii=False, indent=4)

