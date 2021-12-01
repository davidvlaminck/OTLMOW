from enum import Enum


class EnumField:
    def __init__(self, klName):
        self.klName = klName

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'expecting enum {self.klName} in {self.name}')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class KlAIMToestand(Enum):
    in_ontwerp = 1
    gepland = 2
    in_opbouw = 3
    geannuleerd = 4
    in_gebruik = 5
    overgedragen = 6
    uit_gebruik = 7
    verwijderd = 8