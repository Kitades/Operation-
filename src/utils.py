import json

from src.dto import Operation


def get_operation(filename):
    operation = []
    with open(filename, encoding='utf-8') as f:
        for data in json.load(f):
            if data:
                op = Operation.init_from_dict(data)
                operation.append(op)

    return operation