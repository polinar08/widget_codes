import os
import json
import datetime

def load_operations(filename):
    file_path = os.path.join(os.path.dirname(__file__), filename)
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def sort_operations(operations):
    return sorted(operations, key=lambda operation: operation['date'], reverse=True)

def filter_operations(operations):
    return [operation for operation in operations if operation['state'] == 'EXECUTED']

def take_first_n_operations(operations, n=5):
    return operations[:n]

def formatter_date(date):
    date_parts = date.split('T')[0].split('-')
    return '.'.join(date_parts)

def formatter_from(number_from):
    return ' '.join([number_from[:6], '*'*8, number_from[-4:]])

def formatter_to(number_to):
    return '**' + number_to[-4:]