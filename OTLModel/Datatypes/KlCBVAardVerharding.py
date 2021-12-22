from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlCBVAardVerharding(Keuzelijst):
    """Mogelijke waarden voor de aard van de cement/beton verharding."""

    def __init__(self):
        super().__init__(naam="KlCBVAardVerharding",
                         label="CBV aard verharding",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCBVAardVerharding",
                         definition="Mogelijke waarden voor de aard van de cement/beton verharding.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCBVAardVerharding")

        self.add_option("ongewapend-beton", "ongewapend beton", "Verharding van ongewapend beton.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVAardVerharding/ongewapend-beton")
        self.add_option("doorgaand-gewapend-beton", "doorgaand gewapend beton", "Verharding van doorgaand gewapend beton.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVAardVerharding/doorgaand-gewapend-beton")
        self.add_option("gewapend-beton", "gewapend beton", "Verharding van gewapend beton.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVAardVerharding/gewapend-beton")
        self.add_option("staalvezelbeton", "staalvezelbeton", "Verharding van staalvezelbeton.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVAardVerharding/staalvezelbeton")
