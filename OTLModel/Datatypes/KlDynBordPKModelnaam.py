# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordPKModelnaam(Keuzelijst):
    """Keuzelijst met de gangbare modelnamen van dynamische Pijl-Kruis borden. De modelnamen worden meestal door de leverancier of fabrikant bepaald."""

    def __init__(self):
        super().__init__(naam="KlDynBordPKModelnaam",
                         label="Dyn bord PK modelnaam",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordPKModelnaam",
                         definition="Keuzelijst met de gangbare modelnamen van dynamische Pijl-Kruis borden. De modelnamen worden meestal door de leverancier of fabrikant bepaald.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordPKModelnaam")

        self.add_option("PK-Tidal", "PK-Tidal", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordPKModelnaam/PK-Tidal")
        self.add_option("PK-08J03", "PK-08J03", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordPKModelnaam/PK-08J03")
        self.add_option("PK-LHT", "PK-LHT", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordPKModelnaam/PK-LHT")
