import json
note = input('Введите заметку: \n')
with open("data.json", "w", encoding="utf-8") as f:
    json.dump([note], f, ensure_ascii=False, indent=4)
