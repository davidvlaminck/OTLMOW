# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlExternedetectieAangeslotentoestel(Keuzelijst):
    """Keuzelijst met de voorkomende types van aangesloten toestellen (trein, brug, FCD) aan een externe detectie."""

    def __init__(self):
        super().__init__(naam="KlExternedetectieAangeslotentoestel",
                         label="Externedetectie aangeslotentoestel",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlExternedetectieAangeslotentoestel",
                         definition="Keuzelijst met de voorkomende types van aangesloten toestellen (trein, brug, FCD) aan een externe detectie.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlExternedetectieAangeslotentoestel")

        self.add_option("brug", "brug", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/brug")
        self.add_option("tunnel", "tunnel", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/tunnel")
        self.add_option("spoorweg", "spoorweg", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/spoorweg")
        self.add_option("de-Lijn", "de Lijn", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/de-Lijn")
        self.add_option("MIVB", "MIVB", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/MIVB")
        self.add_option("hulpdiensten", "hulpdiensten", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/hulpdiensten")
        self.add_option("militaire-kazerne", "militaire kazerne", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/militaire-kazerne")
        self.add_option("luchthaven", "luchthaven", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/luchthaven")
