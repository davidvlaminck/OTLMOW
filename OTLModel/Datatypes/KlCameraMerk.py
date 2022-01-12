# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCameraMerk(Keuzelijst):
    """Het merk van de camera."""

    def __init__(self):
        super().__init__(naam="KlCameraMerk",
                         label="Camera merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCameraMerk",
                         definition="Het merk van de camera.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCameraMerk")

        self.add_option("bosch", "Bosch", "Bosch", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraMerk/bosch")
        self.add_option("videotec", "Videotec", "Videotec", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraMerk/videotec")
