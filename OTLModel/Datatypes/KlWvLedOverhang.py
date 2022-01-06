# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLedOverhang(Keuzelijst):
    """Afstand tot de rand van de rijbaan van de verticale projectie van het verlichtingstoestel op de rijbaan in meter. Als de afstand tot de rijbaan gelijk is aan 0, dan valt de verticale projectie samen met de rand van de rijbaan, bij negatieve waardes ligt de verticale projectie in de berm en bij positieve waardes ligt de verticale projectie op de rijbaan."""

    def __init__(self):
        super().__init__(naam="KlWvLedOverhang",
                         label="WV LED overhang",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedOverhang",
                         definition="Afstand tot de rand van de rijbaan van de verticale projectie van het verlichtingstoestel op de rijbaan in meter. Als de afstand tot de rijbaan gelijk is aan 0, dan valt de verticale projectie samen met de rand van de rijbaan, bij negatieve waardes ligt de verticale projectie in de berm en bij positieve waardes ligt de verticale projectie op de rijbaan.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedOverhang")

        self.add_option("o+0", "o+0", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+0")
        self.add_option("o-1", "o-1", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-1")
        self.add_option("o-2", "o-2", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-2")
        self.add_option("o-3", "o-3", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-3")
        self.add_option("o-4", "o-4", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-4")
        self.add_option("o-5", "o-5", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-5")
        self.add_option("o+0.5", "o+0.5", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+0.5")
        self.add_option("o+1.5", "o+1.5", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+1.5")
        self.add_option("o+2.5", "o+2.5", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+2.5")
        self.add_option("o+3.5", "o+3.5", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+3.5")
        self.add_option("o+4.5", "o+4.5", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+4.5")
