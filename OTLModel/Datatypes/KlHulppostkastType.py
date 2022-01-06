# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHulppostkastType(Keuzelijst):
    """Lijst met al dan niet gestandaardiseerde types voor hulppostkasten."""

    def __init__(self):
        super().__init__(naam="KlHulppostkastType",
                         label="Hulppostkast type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHulppostkastType",
                         definition="Lijst met al dan niet gestandaardiseerde types voor hulppostkasten.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHulppostkastType")

        self.add_option("a", "a", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulppostkastType/a")
        self.add_option("c", "c", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulppostkastType/c")
