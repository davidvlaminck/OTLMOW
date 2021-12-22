from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlLEGCOpeningType(Keuzelijst):
    """Types van opening."""

    def __init__(self):
        super().__init__(naam="KlLEGCOpeningType",
                         label="Opening type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCOpeningType",
                         definition="Types van opening.",
                         usagenote="Klasse uit gebruik sinds versie 2.1.0",
                         deprecated_version="2.1.0",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCOpeningType")

        self.add_option("nooddeur", "nooddeur", "Deze optie mag niet geselecteerd worden. Indien de doorgang een nooddeur is moet het onderdeel 'Vluchtdeur' geïnstantieerd worden ipv het onderdeel 'Doorgang'.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpeningType/nooddeur")
        self.add_option("vluchtopening", "vluchtopening", "vluchtopening", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpeningType/vluchtopening")
        self.add_option("dienstopening", "dienstopening", "dienstopening", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpeningType/dienstopening")
        self.add_option("sas", "sas", "sas", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpeningType/sas")
