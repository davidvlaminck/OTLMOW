# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSlemlaagsoort(Keuzelijst):
    """Soorten van slemlaag."""

    def __init__(self):
        super().__init__(naam="KlSlemlaagsoort",
                         label="Slemlaagsoort",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSlemlaagsoort",
                         definition="Soorten van slemlaag.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSlemlaagsoort")

        self.add_option("0-10", "0/10", "0/10", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemlaagsoort/0-10")
        self.add_option("0-2", "0/2", "0/2", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemlaagsoort/0-2")
        self.add_option("0-4", "0/4", "0/4", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemlaagsoort/0-4")
        self.add_option("0-6.3", "0/6.3", "0/6,3", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemlaagsoort/0-6.3")
