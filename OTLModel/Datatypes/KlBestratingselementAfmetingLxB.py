# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBestratingselementAfmetingLxB(Keuzelijst):
    """De afmetingen of aanduidingen voor bestrating van betonstraatstenen."""

    def __init__(self):
        super().__init__(naam="KlBestratingselementAfmetingLxB",
                         label="Afmeting bestratingselement lengte x breedte",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBestratingselementAfmetingLxB",
                         definition="De afmetingen of aanduidingen voor bestrating van betonstraatstenen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBestratingselementAfmetingLxB")

        self.add_option("1000-x-1000", "1000 x 1000", "1000 x 1000", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/1000-x-1000")
        self.add_option("150-x-150", "150 x 150", "150 x 150", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/150-x-150")
        self.add_option("200-x-200", "200 x 200", "200 x 200", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/200-x-200")
        self.add_option("200-x-200-voegstenen", "200 x 200 voegstenen", "200 x 200 voegstenen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/200-x-200-voegstenen")
        self.add_option("220-x-110", "220 x 110", "220 x 110", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/220-x-110")
        self.add_option("220-x-220", "220 x 220", "220 x 220", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/220-x-220")
        self.add_option("220-x-220-voegstenen", "220 x 220 voegstenen", "220 x 220 voegstenen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/220-x-220-voegstenen")
        self.add_option("300-x-300", "300 x 300", "300 x 300", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/300-x-300")
        self.add_option("400-x-400", "400 x 400", "400 x 400", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/400-x-400")
        self.add_option("500-x-500", "500 x 500", "500 x 500", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/500-x-500")
        self.add_option("600-x-600", "600 x 600", "600 x 600", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/600-x-600")
        self.add_option("800-x-800", "800 x 800", "800 x 800", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/800-x-800")
        self.add_option("afmetingen-volgens-de-opdrachtdocumenten", "afmetingen volgens de opdrachtdocumenten", "afmetingen volgens de opdrachtdocumenten", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/afmetingen-volgens-de-opdrachtdocumenten")
