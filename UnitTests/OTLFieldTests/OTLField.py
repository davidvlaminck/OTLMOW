from abc import abstractmethod


class OTLField:
    def __init__(self):
        self.naam = ''
        self.label = ''
        self.objectUri = ''
        self.definition = ''
        self.constraints = ''
        self.usagenote = ''

    @abstractmethod
    def validate(self, value, attribuut=None):
        pass