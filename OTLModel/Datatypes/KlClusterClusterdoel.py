from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlClusterClusterdoel(Keuzelijst):
    """De reden waarom de custer is opgezet."""

    def __init__(self):
        super().__init__(naam="KlClusterClusterdoel",
                         label="Cluster clusterdoel",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlClusterClusterdoel",
                         definition="De reden waarom de custer is opgezet.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlClusterClusterdoel")

        self.add_option("redundantie", "redundantie", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlClusterClusterdoel/redundantie")
        self.add_option("groeperen-resources", "groeperen resources", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlClusterClusterdoel/groeperen-resources")
