import json

def load_operations(filename):

    """Загружает операций студентов из файла"""
    with open(filename, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
        return data

def sort_operations(state, dict_):
    executed = []
    for item in dict_:
        if item.get("state") == state:
            executed.append(item)
    return executed

def sort_by_date(data):
    data.sort(key=lambda x: x['date'], reverse=True)
    return data

def convert_date(date):
    date = date[:10]
    date = date.split("-")
    new_date = f'{date[2]}.{date[1]}.{date[0]}'
    return new_date

def mask_card_number(card_number):
    new_card_number = f'{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}'
    return new_card_number
