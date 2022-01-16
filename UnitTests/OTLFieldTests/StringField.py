from UnitTests.OTLFieldTests.OTLField import OTLField


class StringField(OTLField):
    def __init__(self):
        super().__init__()
        self.naam = "StringField"
        self.definition = "Beschrijft een tekstregel volgens http://www.w3.org/2001/XMLSchema#string."

    def validate(value, attribuut):
        if value is not None and not isinstance(value, str):
            raise TypeError(f'expecting string in {attribuut.naam}')
        return True

    def __str__(self):
        return f"naam: {self.naam}; definitie: {self.definition}"
