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