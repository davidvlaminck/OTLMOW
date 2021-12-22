from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlNetwerklinkMediumtype(Keuzelijst):
    """Mogelijke waarden voor het type drager waarlangs data door de link getransporteerd wordt."""

    def __init__(self):
        super().__init__(naam="KlNetwerklinkMediumtype",
                         label="Netwerklink mediumtype",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerklinkMediumtype",
                         definition="Mogelijke waarden voor het type drager waarlangs data door de link getransporteerd wordt.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerklinkMediumtype")

        self.add_option("dsl", "DSL", "De link tussen de netwerkpoorten wordt gerealiseerd via een DSL verbinding.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerklinkMediumtype/dsl")
        self.add_option("transportnetwerk", "transportnetwerk", "De link tussen de netwerkpoorten wordt gerealiseerd via het optisch transportnetwerk.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerklinkMediumtype/transportnetwerk")
        self.add_option("utp", "UTP", "De link tussen de netwerkpoorten wordt gerealiseerd via een UTP kabel.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerklinkMediumtype/utp")
        self.add_option("optisch", "optisch", "De link tussen de netwerkpoorten wordt gerealiseerd via een glasvezelkabel.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerklinkMediumtype/optisch")
        self.add_option("andere", "andere", "De link tussen de netwerkpoorten wordt gerealiseerd via een andere dan een optische, UTP, DSL of transportnetwerk verbinding.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerklinkMediumtype/andere")
