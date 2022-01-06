# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCabineAardingsstelsel(Keuzelijst):
    """Lijst van mogelijke aardinggsstelsels."""

    def __init__(self):
        super().__init__(naam="KlCabineAardingsstelsel",
                         label="Cabine aardingsstelsel",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCabineAardingsstelsel",
                         definition="Lijst van mogelijke aardinggsstelsels.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCabineAardingsstelsel")

        self.add_option("gescheiden", "gescheiden", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineAardingsstelsel/gescheiden")
        self.add_option("globaal", "globaal", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineAardingsstelsel/globaal")
