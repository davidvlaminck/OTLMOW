# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHoutigeType(Keuzelijst):
    """Types van houtige vegetatie."""

    def __init__(self):
        super().__init__(naam="KlHoutigeType",
                         label="Type houtige vegetatie",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHoutigeType",
                         definition="Types van houtige vegetatie.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHoutigeType")

        self.add_option("houtkant", "houtkant", "Een houtkant is een lijnvormige begroeiing met houtgewas (combinatie van bomen en struiken) met een minimale breedte van 3meter en meer en minstens 1 plantrij. ", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHoutigeType/houtkant")
        self.add_option("bomen---bos", "bomen - bos", "Opgaande beplanting van houtachtige gewassen die boomvormend zijn.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHoutigeType/bomen---bos")
