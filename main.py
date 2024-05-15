from src.dto import Operation
from src.utils import get_operation


def main():
    operations = get_operation('operation.json')
    op = Operation.init_from_dict(operations[0])
    print(op)


if __name__ == '__main__':
    main()
