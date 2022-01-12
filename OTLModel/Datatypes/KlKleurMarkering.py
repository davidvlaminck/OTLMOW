# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKleurMarkering(Keuzelijst):
    """De mogeglijke markeringskleuren."""

    def __init__(self):
        super().__init__(naam="KlKleurMarkering",
                         label="Kleur markering",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKleurMarkering",
                         definition="De mogeglijke markeringskleuren.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKleurMarkering")

        self.add_option("geel-(Y1)", "geel (Y1)", "Geel (Y1) als kleur van de markering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurMarkering/geel-(Y1)")
        self.add_option("geel-(Y2)", "geel (Y2)", "Geel (Y2) als kleur van de markering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurMarkering/geel-(Y2)")
        self.add_option("oker-(RAL1024)", "oker (RAL1024)", "Oker als de kleur van de markering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurMarkering/oker-(RAL1024)")
        self.add_option("rood-(RAL3020)", "rood (RAL3020)", "Rood als de kleur van de markering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurMarkering/rood-(RAL3020)")
        self.add_option("wit", "wit", "Wit als de kleur van de markering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurMarkering/wit")
