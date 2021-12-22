from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlEcoPoorttype(Keuzelijst):
    """Types van de poort."""

    def __init__(self):
        super().__init__(naam="KlEcoPoorttype",
                         label="Poorttype",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEcoPoorttype",
                         definition="Types van de poort.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEcoPoorttype")

        self.add_option("enkel", "enkel", "Een enkele poort.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoPoorttype/enkel")
        self.add_option("dubbel", "dubbel", "Een dubble poort.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoPoorttype/dubbel")
