# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLantaarnVormgeving(Keuzelijst):
    """Keuzelijst met verschillende types vormgeving voor een seinlantaarn."""

    def __init__(self):
        super().__init__(naam="KlLantaarnVormgeving",
                         label="Lantaarn vormgeving",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlLantaarnVormgeving",
                         definition="Keuzelijst met verschillende types vormgeving voor een seinlantaarn.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLantaarnVormgeving")

        self.add_option("bijzondere-esthetische-vormgeving", "bijzondere esthetische vormgeving", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLantaarnVormgeving/bijzondere-esthetische-vormgeving")
        self.add_option("standaard-vormgeving", "standaard vormgeving", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLantaarnVormgeving/standaard-vormgeving")
