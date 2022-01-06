# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomtoestandMeerwaardefactor(Keuzelijst):
    """De meerwaarde (ecologisch,erfgoed) van de boom."""

    def __init__(self):
        super().__init__(naam="KlBoomtoestandMeerwaardefactor",
                         label="Boomtoestand meerwaardefactor",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomtoestandMeerwaardefactor",
                         definition="De meerwaarde (ecologisch,erfgoed) van de boom.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomtoestandMeerwaardefactor")

        self.add_option("1", "1", "De boom heeft geen of minder dan 3 specifieke kenmerken die de ecologische en/of erfgoedwaarde verhogen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomtoestandMeerwaardefactor/1")
        self.add_option("15", "15", "De boom heeft minstens 3 kenmerken van ecologische waarde EN/OF erfgoedwaarde OF boom is opgenomen in de Vlaamse wetenschappelijke erfgoedinventaris", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomtoestandMeerwaardefactor/15")
        self.add_option("2", "2", "De boom heeft minstens 4 kenmerken van ecologische EN/OF erfgoedwaarde OF de boom heeft minstens 2 kenmerken van ecologische waarde in combinatie met 1 kenmerk van zeer hoge ecologische waarde; OF de boom maakt deel uit van een (ruimere) bescherming als monument, cultuurhistorisch landschap of stads- en dorpsgezicht", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomtoestandMeerwaardefactor/2")
        self.add_option("25", "25", "De boom is individueel beschermd als monument", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomtoestandMeerwaardefactor/25")
