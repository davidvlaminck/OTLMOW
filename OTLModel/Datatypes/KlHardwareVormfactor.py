from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlHardwareVormfactor(Keuzelijst):
    """Het soort toestel waarin de fysieke componenten of onderdelen worden vormgegeven."""

    def __init__(self):
        super().__init__(naam="KlHardwareVormfactor",
                         label="Hardware vormfactor",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHardwareVormfactor",
                         definition="Het soort toestel waarin de fysieke componenten of onderdelen worden vormgegeven.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHardwareVormfactor")

        self.add_option("server", "server", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareVormfactor/server")
        self.add_option("desktop", "desktop", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareVormfactor/desktop")
        self.add_option("laptop", "laptop", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareVormfactor/laptop")
