from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlWegreflectorType(Keuzelijst):
    """De vormen van een wegreflector."""

    def __init__(self):
        super().__init__(naam="KlWegreflectorType",
                         label="Wegreflector type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWegreflectorType",
                         definition="De vormen van een wegreflector.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWegreflectorType")

        self.add_option("kunststof-wegdekreflector", "kunststof wegdekreflector", "Een kunststoffen wegreflector aangebracht op de rijbaan met als doel de zichtbaarheid van verkeerseilanden te verhogen en geleiding van de weggebruiker langs de weg", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegreflectorType/kunststof-wegdekreflector")
        self.add_option("glasbolreflector-50-mm-diameter", "glasbolreflector 50 mm diameter", "Een wegreflector in glas en diameter 50 millimeter met als doel de geleiding van de weggebruiker langs de weg", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegreflectorType/glasbolreflector-50-mm-diameter")
        self.add_option("metalen-wegdekreflector", "metalen wegdekreflector", "Een metalen wegreflector aangebracht op de rijbaan met als doel de zichtbaarheid van verkeerseilanden te verhogen en geleiding van de weggebruiker langs de weg", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegreflectorType/metalen-wegdekreflector")
        self.add_option("glasbolreflector-100-mm-diameter", "glasbolreflector 100 mm diameter", "Een wegreflector in glas en diameter 100 millimeter met als doel de geleiding van de weggebruiker langs de weg", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegreflectorType/glasbolreflector-100-mm-diameter")
