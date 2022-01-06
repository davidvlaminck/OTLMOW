# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlContactorType(Keuzelijst):
    """Geeft aan of het een K of Q contactor betreft."""

    def __init__(self):
        super().__init__(naam="KlContactorType",
                         label="contactor type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlContactorType",
                         definition="Geeft aan of het een K of Q contactor betreft.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlContactorType")

        self.add_option("K", "K", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlContactorType/K")
        self.add_option("Q", "Q", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlContactorType/Q")
