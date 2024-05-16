from src.dto import Operation
from src.utils import get_operation


def main():
    operations = get_operation('operation.json')
    for op in operations:
        print(op)


if __name__ == '__main__':
    main()
