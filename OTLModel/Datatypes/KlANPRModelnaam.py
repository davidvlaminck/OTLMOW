from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlANPRModelnaam(Keuzelijst):
    """De modelnaam van de ANPR camera."""

    def __init__(self):
        super().__init__(naam="KlANPRModelnaam",
                         label="ANPR modelnaam",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlANPRModelnaam",
                         definition="De modelnaam van de ANPR camera.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlANPRModelnaam")

        self.add_option("G1", "G1", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRModelnaam/G1")
        self.add_option("dual", "dual", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRModelnaam/dual")
        self.add_option("G3", "G3", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRModelnaam/G3")
        self.add_option("i-car-cam5", "iCar cam5", "iCar cam5", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRModelnaam/i-car-cam5")
