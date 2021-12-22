from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlEcoLooprichelType(Keuzelijst):
    """Types van looprichel."""

    def __init__(self):
        super().__init__(naam="KlEcoLooprichelType",
                         label="Looprichel type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEcoLooprichelType",
                         definition="Types van looprichel.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEcoLooprichelType")

        self.add_option("hout", "hout", "Een houten looprichel.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoLooprichelType/hout")
        self.add_option("beton", "beton", "Een betonnen looprichel.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoLooprichelType/beton")
        self.add_option("schanskorven", "schanskorven", "Een oever bestaande uit schanskorven.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoLooprichelType/schanskorven")
        self.add_option("doorlopende-natuurlijke-oever", "doorlopende natuurlijke oever", "Een doorlopende natuurlijke oever.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoLooprichelType/doorlopende-natuurlijke-oever")
