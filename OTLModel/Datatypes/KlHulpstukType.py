from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlHulpstukType(Keuzelijst):
    """Het type van het hulpstuk."""

    def __init__(self):
        super().__init__(naam="KlHulpstukType",
                         label="Hulpstuk type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHulpstukType",
                         definition="Het type van het hulpstuk.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHulpstukType")

        self.add_option("bochtstuk", "bochtstuk", "bochtstuk", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulpstukType/bochtstuk")
        self.add_option("Y-stuk", "Y-stuk", "Y-stuk", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulpstukType/Y-stuk")
        self.add_option("T-stuk", "T-stuk", "T-stuk", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulpstukType/T-stuk")
        self.add_option("aansluitstuk", "aansluitstuk", "aansluitstuk", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulpstukType/aansluitstuk")
