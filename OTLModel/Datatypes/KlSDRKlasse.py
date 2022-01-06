# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSDRKlasse(Keuzelijst):
    """De verhouding tussen de wanddikte en de diameter van de persleiding."""

    def __init__(self):
        super().__init__(naam="KlSDRKlasse",
                         label="SDR klasse",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSDRKlasse",
                         definition="De verhouding tussen de wanddikte en de diameter van de persleiding.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSDRKlasse")

        self.add_option("11", "11", "11", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSDRKlasse/11")
        self.add_option("17", "17", "17", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSDRKlasse/17")
