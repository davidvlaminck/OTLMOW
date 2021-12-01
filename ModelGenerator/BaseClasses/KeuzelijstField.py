from ModelGenerator.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde
from ModelGenerator.BaseClasses.Keuzelijst import Keuzelijst


class KeuzelijstField:
    keuzelijst: Keuzelijst
    value: KeuzelijstWaarde = None

    def __init__(self, keuzelijst: Keuzelijst):
        self.keuzelijst = keuzelijst

    def get_options(self):
        return self.keuzelijst.options

    def set_value_by_waarde(self, waarde):
        try:
            self.value = next(o for o in self.keuzelijst.options if o.waarde == waarde)
        except StopIteration:
            raise ValueError(f"There is no option with waarde '{waarde}' in {self.keuzelijst.naam}.")

    def set_value_by_label(self, label):
        try:
            self.value = next(o for o in self.keuzelijst.options if o.label == label)
        except StopIteration:
            raise ValueError(f"There is no option with label '{label}' in {self.keuzelijst.naam}.")
