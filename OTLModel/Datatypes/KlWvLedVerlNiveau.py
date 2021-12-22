from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlWvLedVerlNiveau(Keuzelijst):
    """Een set van verlichtingstechnische eisen zoals gemiddelde luminantie, verlichtingsterkte, uniformeiten."""

    def __init__(self):
        super().__init__(naam="KlWvLedVerlNiveau",
                         label="WV LED verlichtingsniveau",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedVerlNiveau",
                         definition="Een set van verlichtingstechnische eisen zoals gemiddelde luminantie, verlichtingsterkte, uniformeiten.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedVerlNiveau")

        self.add_option("M2", "M2", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/M2")
        self.add_option("M3", "M3", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/M3")
        self.add_option("M4", "M4", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/M4")
        self.add_option("P3", "P3", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/P3")
        self.add_option("P4", "P4", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/P4")
        self.add_option("P5", "P5", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/P5")
        self.add_option("C1", "C1", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/C1")
        self.add_option("C2", "C2", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/C2")
        self.add_option("C3", "C3", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/C3")
        self.add_option("C4", "C4", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/C4")
        self.add_option("ZR", "ZR", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/ZR")
        self.add_option("ZL", "ZL", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/ZL")
