import json
import datetime
import os


def load_operations(filename):
    file_path = os.path.join(os.path.dirname(__file__), filename)
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def sort_operations(operations):
    return sorted(operations, key=lambda operation: operation['date'], reverse=True)


def filter_operations(operations):
    return [operation for operation in operations if operation.get('state') == 'EXECUTED']


def take_first_n_operations(operations, n=5):
    return operations[:n]


def formatter_date(date):
    formatted_date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
    return formatted_date


def formatter_from(number_from):
    return ' '.join([number_from[:6], '*' * 8, number_from[-4:]])


def formatter_to(number_to):
    return '**' + number_to[-4:]
