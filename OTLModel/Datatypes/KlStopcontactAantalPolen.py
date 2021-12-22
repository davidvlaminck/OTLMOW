from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlStopcontactAantalPolen(Keuzelijst):
    """Mogelijke waarden voor het aantal polen van een stopcontact."""

    def __init__(self):
        super().__init__(naam="KlStopcontactAantalPolen",
                         label="stopcontact aantal polen",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStopcontactAantalPolen",
                         definition="Mogelijke waarden voor het aantal polen van een stopcontact.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStopcontactAantalPolen")

        self.add_option("3P", "3P", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStopcontactAantalPolen/3P")
        self.add_option("4P", "4P", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStopcontactAantalPolen/4P")
