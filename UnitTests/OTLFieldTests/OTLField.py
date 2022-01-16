from abc import abstractmethod


class OTLField:
    def __init__(self):
        self.naam = ''
        self.label = ''
        self.objectUri = ''
        self.definition = ''
        self.constraints = ''
        self.usagenote = ''

    @staticmethod
    @abstractmethod
    def validate(value, attribuut):
        pass
