import json

note = input('Привет! Это менеджер заметок. \n' \
'Введите свою заметку \n'
'1 - Посмотреть мои заметки \n')
if note == '1':
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        print("Ваши заметки:")
        for item in data:
            print(f"- {item}")
else:
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump([note], f, ensure_ascii=False, indent=4)
