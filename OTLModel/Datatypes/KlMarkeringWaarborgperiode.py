# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMarkeringWaarborgperiode(Keuzelijst):
    """Opties om de waarborgperiode aan te duiden."""

    def __init__(self):
        super().__init__(naam="KlMarkeringWaarborgperiode",
                         label="markeringswaarborgperiode",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMarkeringWaarborgperiode",
                         definition="Opties om de waarborgperiode aan te duiden.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMarkeringWaarborgperiode")

        self.add_option("1-jaar", "1 jaar", "Waarborgperiode van 1 jaar.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringWaarborgperiode/1-jaar")
        self.add_option("3-jaar", "3 jaar", "Waarborgperiode van 3 jaar.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringWaarborgperiode/3-jaar")
        self.add_option("6-jaar", "6 jaar", "Waarborgperiode van 6 jaar.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringWaarborgperiode/6-jaar")
