from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlLEACPerformantieniveau(Keuzelijst):
    """De verschillende performantieniveaus van de afschermende constructies."""

    def __init__(self):
        super().__init__(naam="KlLEACPerformantieniveau",
                         label="Performantieniveau",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACPerformantieniveau",
                         definition="De verschillende performantieniveaus van de afschermende constructies.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACPerformantieniveau")

        self.add_option("50", "50", "Obstakelbeveiliger beperkt getest aan 50km/h", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieniveau/50")
        self.add_option("80", "80", "Obstakelbeveiliger getest aan 80km/h", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieniveau/80")
        self.add_option("100", "100", "Obstakelbeveiliger getest aan 100km/h", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieniveau/100")
        self.add_option("110", "110", "Obstakelbeveiliger getest aan 110km/h", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieniveau/110")
        self.add_option("80-1", "80-1", "Obstakelbeveiliger beperkt getest aan 80km/h ", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieniveau/80-1")
