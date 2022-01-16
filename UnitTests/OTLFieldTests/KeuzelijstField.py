from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde
from UnitTests.OTLFieldTests.OTLField import OTLField


class KeuzelijstField(OTLField):
    @staticmethod
    def validate(value, attribuut):
        if not isinstance(value, str):
            raise TypeError(f'{value} is not the correct type. Expecting a string')
        if value is not None and not value in list(map(lambda x: x.invulwaarde, attribuut.field.options)):
            raise ValueError(
                f'{value} is not a valid option for {attribuut.naam}, find the valid options using .attr_type_info("{attribuut.naam}")')
        return True

    def __init__(self, naam, label, objectUri, definition, usagenote, deprecated_version, codelist):
        super().__init__()
        self.options = []
        self.codelist = codelist
        self.naam = naam
        self.label = label
        self.objectUri = objectUri
        self.definition = definition
        self.usagenote = usagenote
        self.deprecated_version = deprecated_version

    def add_option(self, invulwaarde, label, definitie, objectUri):
        waarde = KeuzelijstWaarde()
        waarde.invulwaarde = invulwaarde
        waarde.label = label
        waarde.definitie = definitie
        waarde.objectUri = objectUri
        self.options.append(waarde)

    def __str__(self):
        s = f"naam: {self.naam}; definitie: {self.definition} mogelijke waardes:\n"
        s += '\n'.join(list(map(lambda x: x.invulwaarde, self.options)))
        return s