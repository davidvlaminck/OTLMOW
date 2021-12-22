from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlKabelmofType(Keuzelijst):
    """Types voor kabel- en leidingmoffen."""

    def __init__(self):
        super().__init__(naam="KlKabelmofType",
                         label="Kabelmof type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKabelmofType",
                         definition="Types voor kabel- en leidingmoffen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKabelmofType")

        self.add_option("gietmof", "gietmof", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmofType/gietmof")
        self.add_option("geldoos", "geldoos", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmofType/geldoos")
