# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSlemProductfamilie(Keuzelijst):
    """De mogelijke productfamiles."""

    def __init__(self):
        super().__init__(naam="KlSlemProductfamilie",
                         label="Productfamilies",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSlemProductfamilie",
                         definition="De mogelijke productfamiles.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSlemProductfamilie")

        self.add_option("1", "1", "Productfamilie 1", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemProductfamilie/1")
        self.add_option("2", "2", "Productfamilie 2", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemProductfamilie/2")
        self.add_option("5", "5", "Productfamilie 5", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemProductfamilie/5")
        self.add_option("6", "6", "Productfamilie 6", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemProductfamilie/6")
