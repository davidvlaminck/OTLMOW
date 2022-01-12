# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSierbeplContainer(Keuzelijst):
    """Verschillende mogeliike pot- en containermaten voor de sierbeplanting."""

    def __init__(self):
        super().__init__(naam="KlSierbeplContainer",
                         label="Sierbeplanting container",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSierbeplContainer",
                         definition="Verschillende mogeliike pot- en containermaten voor de sierbeplanting.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSierbeplContainer")

        self.add_option("C10", "C10", "C10", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/C10")
        self.add_option("C5", "C5", "C5", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/C5")
        self.add_option("C7.5", "C7.5", "C7,5", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/C7.5")
        self.add_option("P10.5-C1", "P10.5-C1", "P10,5/C1", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/P10.5-C1")
        self.add_option("P13-C1.2", "P13-C1.2", "P13/C1,2", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/P13-C1.2")
        self.add_option("P14-C1.5", "P14-C1.5", "P14/C1,5", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/P14-C1.5")
        self.add_option("P15-C2", "P15-C2", "P15/C2", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/P15-C2")
        self.add_option("P17-C3", "P17-C3", "P17/C3", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/P17-C3")
        self.add_option("P19-C4", "P19-C4", "P19/C4", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/P19-C4")
        self.add_option("P7", "P7", "P7", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/P7")
        self.add_option("P9", "P9", "P9", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/P9")
