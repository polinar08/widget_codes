from utilis import load_operations, sort_operations, filter_operations, take_first_n_operations, formatter_date, formatter_from, formatter_to

def main():
    filename = 'operations.json'
    operations = load_operations(filename)
    operations = filter_operations(operations)
    operations = sort_operations(operations)
    operations = take_first_n_operations(operations)

    for operation in operations:
        print(formatter_date(operation['date']), operation['description'])
        print(formatter_from(operation.get('from', '')), '->', formatter_to(operation['to']))
        print()

if __name__ == "__main__":
    main()