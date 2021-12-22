from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlBSSType(Keuzelijst):
    """Types van betonstraatsteen en betontegel."""

    def __init__(self):
        super().__init__(naam="KlBSSType",
                         label="BSS type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBSSType",
                         definition="Types van betonstraatsteen en betontegel.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBSSType")

        self.add_option("grijze", "grijze", "Grijze betonstraatstenen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBSSType/grijze")
        self.add_option("gekleurde-met-anorganische-pigmenten", "gekleurde met anorganische pigmenten", "Gekleurde betonstraatstenen met anorganische pigmenten.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBSSType/gekleurde-met-anorganische-pigmenten")
        self.add_option("gekleurde-met-kleurondersteunende-granulaten", "gekleurde met kleurondersteunende granulaten", "Gekleurde betonstraatstenen met kleurondersteunende granulaten.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBSSType/gekleurde-met-kleurondersteunende-granulaten")
        self.add_option("witte-met-kleurondersteunende-granulaten", "witte met kleurondersteunende granulaten", "Witte betonstraatstenen met kleurondersteunende granulaten.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBSSType/witte-met-kleurondersteunende-granulaten")
