from utilis import load_operations, sort_operations, filter_operations, take_first_n_operations, formatter_date, \
    formatter_from, formatter_to


def main():
    filename = 'operations.json'
    operations = load_operations(filename)
    operations = filter_operations(operations)
    operations = sort_operations(operations)
    operations = take_first_n_operations(operations)

    for operation in operations:
        formatted_date = formatter_date(operation['date'])
        formatted_description = operation['description']
        formatted_from = formatter_from(operation.get('from', ''))
        formatted_to = formatter_to(operation['to'])
        amount = float(operation['operationAmount']['amount'])
        currency = operation['operationAmount']['currency']['name']

        print(f"{formatted_date} {formatted_description}")
        print(f"{formatted_from} -> {formatted_to}")
        print(f"{amount:.2f} {currency}")
        print()


if __name__ == "__main__":
    main()