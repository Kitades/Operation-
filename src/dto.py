from datetime import datetime


class Payment:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    @classmethod
    def init_from_str(cls, payment):
        *name, number = payment.split(' ')
        return cls(''.join(name), number)

    def __repr__(self):
        return f'Payment(name={self.name}, number={self.number})'


class Amount:
    def __init__(self, value, currency_name, currency_code):
        self.value = value
        self.currency_name = currency_name
        self.currency_code = currency_code

    def __repr__(self):
        return (
            f'Amount(value={self.value},'
            f'currency_name={self.currency_name},'
            f'currency_code={self.currency_code})'
            )


class Operation:
    def __init__(
            self,
            operation_id,
            state,
            operation_date,
            amount,
            description,
            payment_to,
            payment_from=None
    ):
        self.id = operation_id
        self.state = state
        self.operation_date = operation_date
        self.amount = amount
        self.description = description
        self.payment_to = payment_to
        self.payment_from = payment_from

    @classmethod
    def init_from_dict(cls, data):
        return cls(
            operation_id=int(data['id']),
            state=data['state'],
            operation_date=datetime.fromisoformat(data['date']),
            amount=Amount(
                value=float(data['operationAmount']['amount']),
                currency_name=data['operationAmount']['currency']['name'],
                currency_code=data['operationAmount']['currency']['code']
            ),
            description=data['description'],
            payment_to=Payment.init_from_str(data['to']),
            payment_from=Payment.init_from_str(data['from'])
            if 'from' in data else None,

        )

    def __repr__(self):
        return (
            f'Operation{self.id},'
            f'description{self.description}'
            f'state={self.state},'
            f'date={self.operation_date}'
            f'amount={self.amount}',
            f'from={self.payment_from}',
            f'to={self.payment_to}'
            )
