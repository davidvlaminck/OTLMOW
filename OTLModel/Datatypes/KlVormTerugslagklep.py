from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlVormTerugslagklep(Keuzelijst):
    """De vorm van opening van de terugslagklep."""

    def __init__(self):
        super().__init__(naam="KlVormTerugslagklep",
                         label="Vorm terugslagklep",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVormTerugslagklep",
                         definition="De vorm van opening van de terugslagklep.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVormTerugslagklep")

        self.add_option("circkelvormig", "circkelvormig", "circkelvormig", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormTerugslagklep/circkelvormig")
        self.add_option("rechthoekig", "rechthoekig", "rechthoekig", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormTerugslagklep/rechthoekig")
        self.add_option("andere", "andere", "andere", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormTerugslagklep/andere")
