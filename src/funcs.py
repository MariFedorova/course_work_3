import json

def load_operations(filename):

    """
    загружает список всех операций
    :param filename: имя файла
    :return: загруженный список
    """
    with open(filename, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
        return data

def sort_operations(state, dict_):
    """
    выделяет выполненные опреации
    :param state: статус
    :param dict_: откуда берется информация
    :return: список исполненных
    """
    executed = []
    for item in dict_:
        if item.get("state") == state:
            executed.append(item)
    return executed

def sort_by_date(data):
    """
    сортирует с помощью анонимной функции по дате операции
    :param data: данные для сортировки
    :return: отсортированные данные
    """
    data.sort(key=lambda x: x['date'], reverse=True)
    return data

def convert_date(date):
    """
    делает дату читаемой для соритровки по дате
    :param date: дата
    :return: дата в удобном виде
    """
    date = date[:10]
    date = date.split("-")
    new_date = f'{date[2]}.{date[1]}.{date[0]}'
    return new_date

def mask_card_number(card_number):
    """
    маскирует номер карты
    :param card_number: номер карты
    :return: замаскированный номер карты
    """
    new_card_number = f'{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}'
    return new_card_number


def mask_account_number(acc_number):
    """
    маскирует номер счета
    :param acc_number: номер счета
    :return: замаскированный номер счета
    """
    new_acc_number = f'**{acc_number[-4:]}'
    return new_acc_number