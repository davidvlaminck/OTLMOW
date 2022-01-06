# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSchoorhoek(Keuzelijst):
    """De schoorhoek van het object, uitgedrukt in 1 op x (vb.: 1/4)."""

    def __init__(self):
        super().__init__(naam="KlSchoorhoek",
                         label="Schoorhoek",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlSchoorhoek",
                         definition="De schoorhoek van het object, uitgedrukt in 1 op x (vb.: 1/4).",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSchoorhoek")

        self.add_option("1-3", "1/3", "Een schoorhoek van 1 op 3.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchoorhoek/1-3")
        self.add_option("1-4", "1/4", "Een schoorhoek van 1 op 4.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchoorhoek/1-4")
