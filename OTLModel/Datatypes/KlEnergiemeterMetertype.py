from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlEnergiemeterMetertype(Keuzelijst):
    """Type meter (mechanisch, elektronisch)."""

    def __init__(self):
        super().__init__(naam="KlEnergiemeterMetertype",
                         label="Elektrisch metertype",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlEnergiemeterMetertype",
                         definition="Type meter (mechanisch, elektronisch).",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEnergiemeterMetertype")

        self.add_option("mechanisch", "mechanisch", "Nakijken bij EVT", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEnergiemeterMetertype/mechanisch")
        self.add_option("elektronisch", "elektronisch", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEnergiemeterMetertype/elektronisch")
