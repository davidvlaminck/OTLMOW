from ModelGenerator.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde
from ModelGenerator.BaseClasses.Keuzelijst import Keuzelijst


class KeuzelijstField:
    def __init__(self, keuzelijst: Keuzelijst, value: KeuzelijstWaarde = None):
        self.keuzelijst: Keuzelijst = keuzelijst
        self.value: KeuzelijstWaarde = value

    def getOptions(self):
        return self.keuzelijst.options

    def setValueByWaarde(self, waarde):
        try:
            self.value = next(o for o in self.keuzelijst.options if o.waarde == waarde)
        except StopIteration:
            raise ValueError(f"There is no option with waarde '{waarde}' in {self.keuzelijst.naam}.")

    def setValueByLabel(self, label):
        try:
            self.value = next(o for o in self.keuzelijst.options if o.label == label)
        except StopIteration:
            raise ValueError(f"There is no option with label '{label}' in {self.keuzelijst.naam}.")
