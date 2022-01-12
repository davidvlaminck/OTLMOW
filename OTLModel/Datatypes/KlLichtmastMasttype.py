# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLichtmastMasttype(Keuzelijst):
    """Lijst van mogelijke types voor lichtmasten."""

    def __init__(self):
        super().__init__(naam="KlLichtmastMasttype",
                         label="lichtmast type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLichtmastMasttype",
                         definition="Lijst van mogelijke types voor lichtmasten.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLichtmastMasttype")

        self.add_option("B", "B", "Betonnen paal", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasttype/B")
        self.add_option("BS", "BS", "Betonnen paal op voet", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasttype/BS")
        self.add_option("K", "K", "Kreukelpaal met arm", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasttype/K")
        self.add_option("KS", "KS", "Kreukelpaal met arm op voet", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasttype/KS")
        self.add_option("M", "M", "Metalen paal met arm", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasttype/M")
        self.add_option("MS", "MS", "Metalen paal met arm en voet", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasttype/MS")
        self.add_option("RK", "RK", "Kreukelpaal", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasttype/RK")
        self.add_option("RKS", "RKS", "Kreukelpaal op voet", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasttype/RKS")
        self.add_option("RM", "RM", "Rechte metalen paal", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasttype/RM")
        self.add_option("RMS", "RMS", "Rechte metalen paal op voet", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasttype/RMS")
