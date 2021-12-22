from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlWBSSType(Keuzelijst):
    """Types van waterdoorlatende betonstraatstenen en betontegels."""

    def __init__(self):
        super().__init__(naam="KlWBSSType",
                         label="WBSS type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWBSSType",
                         definition="Types van waterdoorlatende betonstraatstenen en betontegels.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWBSSType")

        self.add_option("grijze", "grijze", "grijze waterdoorlatende betonstraatstenen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWBSSType/grijze")
        self.add_option("gekleurde-met-anorganische-pigmenten", "gekleurde met anorganische pigmenten", "gekleurde waterdoorlatende betonstraatstenen met anorganische pigmenten", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWBSSType/gekleurde-met-anorganische-pigmenten")
        self.add_option("gekleurde-met-kleurondersteunende-granulaten", "gekleurde met kleurondersteunende granulaten", "gekleurde waterdoorlatende betonstraatstenen met kleurondersteunende granulaten", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWBSSType/gekleurde-met-kleurondersteunende-granulaten")
        self.add_option("witte-met-kleurondersteunende-granulaten", "witte met kleurondersteunende granulaten", "witte waterdoorlatende betonstraatstenen met kleurondersteunende granulaten", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWBSSType/witte-met-kleurondersteunende-granulaten")
        self.add_option("waterdoorlatende-betontegel", "waterdoorlatende betontegel", "waterdoorlatende betontegel", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWBSSType/waterdoorlatende-betontegel")
