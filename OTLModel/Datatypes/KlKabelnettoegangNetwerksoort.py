# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKabelnettoegangNetwerksoort(Keuzelijst):
    """Lijst van netwerktypes die bereikbaar is via het kabelnet toegangspunt."""

    def __init__(self):
        super().__init__(naam="KlKabelnettoegangNetwerksoort",
                         label="Kabelnet toegang netwerksoort",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKabelnettoegangNetwerksoort",
                         definition="Lijst van netwerktypes die bereikbaar is via het kabelnet toegangspunt.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKabelnettoegangNetwerksoort")

        self.add_option("Cu", "Cu", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelnettoegangNetwerksoort/Cu")
        self.add_option("FO", "FO", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelnettoegangNetwerksoort/FO")
