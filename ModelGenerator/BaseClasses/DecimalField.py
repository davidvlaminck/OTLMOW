import decimal


class DecimalField:
    def __get__(self, instance, owner):
        try:
            return instance.__dict__[self.name]
        except KeyError:
            return None

    def __set__(self, instance, value):
        if not value is None and not isinstance(value, decimal.Decimal):
            raise ValueError(f'expecting decimal in {self.name}')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name