# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRetroreflecterendVerkeersbordGrootteorde(Keuzelijst):
    """Opties om de grootteorde van een RetroreflecterendVerkeersbord aan te geven zoals gedefinieerd in SB250."""

    def __init__(self):
        super().__init__(naam="KlRetroreflecterendVerkeersbordGrootteorde",
                         label="Retroreflecterend verkeersbord grootteorde",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRetroreflecterendVerkeersbordGrootteorde",
                         definition="Opties om de grootteorde van een RetroreflecterendVerkeersbord aan te geven zoals gedefinieerd in SB250.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRetroreflecterendVerkeersbordGrootteorde")

        self.add_option("klein", "klein", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRetroreflecterendVerkeersbordGrootteorde/klein")
        self.add_option("middelgroot", "middelgroot", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRetroreflecterendVerkeersbordGrootteorde/middelgroot")
        self.add_option("groot", "groot", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRetroreflecterendVerkeersbordGrootteorde/groot")
