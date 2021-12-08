import math


# TODO inherit from OTL Field

class KardinaliteitField:
    name = 'KardinaliteitField'

    def __init__(self, fieldType, minKardinaliteit, maxKardinaliteit):
        self._type = fieldType
        self.minKardinaliteit = minKardinaliteit
        if maxKardinaliteit == '*':
            self.maxKardinaliteit = math.inf
        else:
            self.maxKardinaliteit = maxKardinaliteit

    def __get__(self, instance, owner):
        try:
            return instance.__dict__[self.name]
        except KeyError:
            return None

    def check_types_in_tuple(self, valueList) -> bool:
        bad_type = False
        for el in valueList:
            if not (isinstance(el, self._type)):
                bad_type = True
                return bad_type
        return bad_type

    def __set__(self, instance, value):
        if value is None:
            instance.__dict__[self.name] = value
            return
        elif not isinstance(value, tuple):
            raise ValueError(f'expecting tuple in {self.name}')
        elif len(value) < self.minKardinaliteit:
            raise ValueError(f'expecting at least {self.minKardinaliteit} element(s) in {self.name}')
        elif len(value) > self.maxKardinaliteit:
            raise ValueError(f'expecting at most {self.maxKardinaliteit} element(s) in {self.name}')
        badtype = self.check_types_in_tuple(value)
        if badtype:
            raise ValueError(f'element of bad type in {self.name}')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name
