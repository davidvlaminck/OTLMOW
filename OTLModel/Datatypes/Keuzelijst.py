from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


class Keuzelijst:
    def __init__(self, naam, label, uri, definition, usagenote, deprecated_version, codelist):
        self.options = []
        self.codelist = codelist
        self.naam = naam
        self.label = label
        self.uri = uri
        self.definition = definition
        self.usagenote = usagenote
        self.deprecated_version = deprecated_version

    def add_option(self, invulwaarde, label, definitie, uri):
        waarde = KeuzelijstWaarde()
        waarde.invulwaarde = invulwaarde
        waarde.label = label
        waarde.definitie = definitie
        waarde.uri = uri
        self.options.append(waarde)

    def get_value_by_invulwaarde(self, invulwaarde):
        try:
            return next(o for o in self.options if o.invulwaarde == invulwaarde)
        except StopIteration:
            raise ValueError(f"There is no option with waarde '{invulwaarde}' in {self.naam}.")

    def get_value_by_label(self, label):
        try:
            return next(o for o in self.options if o.label == label)
        except StopIteration:
            raise ValueError(f"There is no option with label '{label}' in {self.naam}.")