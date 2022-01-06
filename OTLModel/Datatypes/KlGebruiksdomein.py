# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGebruiksdomein(Keuzelijst):
    """De omstandigheden waarin het beton gebruikt zal worden."""

    def __init__(self):
        super().__init__(naam="KlGebruiksdomein",
                         label="Gebruiksdomein",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlGebruiksdomein",
                         definition="De omstandigheden waarin het beton gebruikt zal worden.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGebruiksdomein")

        self.add_option("ob-ongewapend", "OB (ongewapend)", "Ongewapend beton.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruiksdomein/ob-ongewapend")
        self.add_option("gb-gewapend", "GB (gewapend)", "Gewapend beton.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruiksdomein/gb-gewapend")
        self.add_option("vb-voorgespannen", "VB (voorgespannen)", "Voorgespannen beton.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruiksdomein/vb-voorgespannen")
