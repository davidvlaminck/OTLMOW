from ModelGenerator.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


class KeuzelijstField:
    value: KeuzelijstWaarde = None

    def __init__(self, naam, label, uri):
        self.naam = naam
        self.label = label
        self.uri = uri
        self.options = []

    def add_option(self, waarde, label, definitie, uri):
        self.options.append(KeuzelijstWaarde(waarde, label, definitie, uri))

    def get_options(self):
        return self.options

    def set_value_by_waarde(self, waarde):
        try:
            self.value = next(o for o in self.options if o.waarde == waarde)
        except StopIteration:
            raise ValueError(f"There is no option with waarde '{waarde}' in {self.naam}.")

    def set_value_by_label(self, label):
        try:
            self.value = next(o for o in self.options if o.label == label)
        except StopIteration:
            raise ValueError(f"There is no option with label '{label}' in {self.naam}.")

    def set_value_by_label_on_init(self, optionByLabel: str):
        if optionByLabel is not None:
            self.set_value_by_label(optionByLabel)
