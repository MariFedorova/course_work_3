from funcs import load_operations, sort_operations, sort_by_date, convert_date, mask_card_number, mask_account_number

file = 'operations.json'

load_operations = load_operations(file)

s = "EXECUTED"

result = sort_operations("EXECUTED", load_operations)

result_sorted = sort_by_date(result)

final_operations = result_sorted[:5]

for item in final_operations:
    date = item.get("date")
    description = item.get("description")
    from_ = item.get("from")
    to_ = item.get("to")
    amount = item.get("operationAmount").get("amount")
    currency = item.get("operationAmount").get("currency").get("name")

    date = convert_date(date)
    if not from_:
        name_from_ = ""
        hidden_from_number = "отправитель не указан"
    elif "Счет" in from_:
        name_from_ = "Счет"
        hidden_from_number = mask_account_number(from_[-20:])
    else:
        name_from_ = from_[:-17]
        hidden_from_number = mask_card_number(from_[-16:])

    to_ = mask_account_number(to_[-20:])

    print(f'''{date} {description}
{name_from_} {hidden_from_number} -> Счет {to_}
{amount} {currency}''')



