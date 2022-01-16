from abc import abstractmethod

from UnitTests.OTLFieldTests.OTLField import OTLField


class ComplexField(OTLField):
    @abstractmethod
    def __init__(self):
        super().__init__()

    @staticmethod
    def validate(value, attribuut):
        if value is not None and not isinstance(value, str):
            raise TypeError(f'expecting string in {attribuut.naam}')
        return True

    def __str__(self):
        return f"naam: {self.naam}; definitie: {self.definition}"