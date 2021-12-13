from ModelGenerator.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde
from ModelGenerator.BaseClasses.OTLField import OTLField


class KeuzelijstField(OTLField):
    def __init__(self, naam, label, uri, definition, constraints, usagenote, deprecated_version, codelist, readonly=False, readonlyValue=None):
        super().__init__(naam, label, uri, definition, constraints, usagenote, deprecated_version, readonly, readonlyValue)
        self.options = []
        self.codelist = codelist
        self.waarde: KeuzelijstWaarde = None

    def add_option(self, invulwaarde, label, definitie, uri):
        self.options.append(KeuzelijstWaarde(invulwaarde, label, definitie, uri))

    def get_options(self):
        return self.options

    def set_value_by_invulwaarde(self, invulwaarde):
        try:
            self.waarde = next(o for o in self.options if o.invulwaarde == invulwaarde)
        except StopIteration:
            raise ValueError(f"There is no option with waarde '{invulwaarde}' in {self.naam}.")

    def set_value_by_label(self, label):
        try:
            self.waarde = next(o for o in self.options if o.label == label)
        except StopIteration:
            raise ValueError(f"There is no option with label '{label}' in {self.naam}.")

    def set_value_by_label_on_init(self, optionByLabel: str):
        if optionByLabel is not None:
            self.set_value_by_label(optionByLabel)

    def __getstate__(self):
        return self.waarde
