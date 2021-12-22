from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlAlgSnelheidsregime(Keuzelijst):
    """De snelheidsregimes met variabele mogelijkeid."""

    def __init__(self):
        super().__init__(naam="KlAlgSnelheidsregime",
                         label="Snelheidsregime",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAlgSnelheidsregime",
                         definition="De snelheidsregimes met variabele mogelijkeid.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgSnelheidsregime")

        self.add_option("30", "30", "30 km/h.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/30")
        self.add_option("90", "90", "90 km/h.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/90")
        self.add_option("50", "50", "50 km/h.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/50")
        self.add_option("variabel", "variabel", "Variabele ingave.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/variabel")
        self.add_option("60", "60", "60 km/h.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/60")
        self.add_option("120", "120", "120 km/h.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/120")
        self.add_option("70", "70", "70 km/h.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/70")
        self.add_option("80", "80", "80 km/h.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/80")
