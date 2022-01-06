# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDolomietType(Keuzelijst):
    """Types van dolomiet."""

    def __init__(self):
        super().__init__(naam="KlDolomietType",
                         label="Dolomiet type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDolomietType",
                         definition="Types van dolomiet.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDolomietType")

        self.add_option("0-5", "0-5", "0/5", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDolomietType/0-5")
        self.add_option("0-15", "0-15", "0/15", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDolomietType/0-15")
        self.add_option("5-15", "5-15", "mei-15", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDolomietType/5-15")
