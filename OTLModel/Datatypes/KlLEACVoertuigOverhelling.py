# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACVoertuigOverhelling(Keuzelijst):
    """De verschillende maten van voertuigoverhelling."""

    def __init__(self):
        super().__init__(naam="KlLEACVoertuigOverhelling",
                         label="Voertuig overhelling",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACVoertuigOverhelling",
                         definition="De verschillende maten van voertuigoverhelling.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACVoertuigOverhelling")

        self.add_option("vIn1", "vIn1", "VIn <= 0.6", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACVoertuigOverhelling/vIn1")
        self.add_option("vIn2", "vIn2", "VIn <= 0.8", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACVoertuigOverhelling/vIn2")
        self.add_option("vIn3", "vIn3", "VIn <= 1.0", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACVoertuigOverhelling/vIn3")
        self.add_option("vIn4", "vIn4", "VIn <= 1.3", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACVoertuigOverhelling/vIn4")
        self.add_option("vIn5", "vIn5", "VIn <= 1.7", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACVoertuigOverhelling/vIn5")
        self.add_option("vIn6", "vIn6", "VIn <= 2.1", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACVoertuigOverhelling/vIn6")
        self.add_option("vIn7", "vIn7", "VIn <= 2.5", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACVoertuigOverhelling/vIn7")
        self.add_option("vIn8", "vIn8", "VIn <= 3.5", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACVoertuigOverhelling/vIn8")
        self.add_option("vIn9", "vIn9", "VIn > 3.5", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACVoertuigOverhelling/vIn9")
