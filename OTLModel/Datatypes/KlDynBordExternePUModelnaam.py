# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordExternePUModelnaam(Keuzelijst):
    """De modelnaam van externe processing unit voor dynamische verkeersborden. Wordt bepaald door de lverancier."""

    def __init__(self):
        super().__init__(naam="KlDynBordExternePUModelnaam",
                         label="Keuzelijst met modellen van Externe PU",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordExternePUModelnaam",
                         definition="De modelnaam van externe processing unit voor dynamische verkeersborden. Wordt bepaald door de lverancier.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordExternePUModelnaam")

        self.add_option("diamond", "diamond", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordExternePUModelnaam/diamond")
        self.add_option("ixor", "ixor", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordExternePUModelnaam/ixor")
        self.add_option("moxa", "moxa", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordExternePUModelnaam/moxa")
