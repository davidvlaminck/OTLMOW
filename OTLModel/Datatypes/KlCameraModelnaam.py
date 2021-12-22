from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlCameraModelnaam(Keuzelijst):
    """De modelnaam van de camera."""

    def __init__(self):
        super().__init__(naam="KlCameraModelnaam",
                         label="Camera modelnaam",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCameraModelnaam",
                         definition="De modelnaam van de camera.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCameraModelnaam")

        self.add_option("dinion-ip-starlight-8000-m", "Dinion IP Starlight 8000 M", "Dinion IP Starlight 8000 M", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/dinion-ip-starlight-8000-m")
        self.add_option("ulisse-hd", "Ulisse HD", "Ulisse HD", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/ulisse-hd")
