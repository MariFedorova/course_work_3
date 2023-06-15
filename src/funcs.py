import json

def load_operations(filename):

    """Загружает операций студентов из файла"""
    with open(filename, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
        return data