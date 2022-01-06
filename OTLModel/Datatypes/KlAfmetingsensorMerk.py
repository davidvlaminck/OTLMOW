# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfmetingsensorMerk(Keuzelijst):
    """Het merk van de afmetingsensor."""

    def __init__(self):
        super().__init__(naam="KlAfmetingsensorMerk",
                         label="Afmetingsensor merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfmetingsensorMerk",
                         definition="Het merk van de afmetingsensor.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfmetingsensorMerk")

        self.add_option("Sick", "Sick", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfmetingsensorMerk/Sick")
