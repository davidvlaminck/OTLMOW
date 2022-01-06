# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfmetingsensorType(Keuzelijst):
    """Het type van de afmetingsensor."""

    def __init__(self):
        super().__init__(naam="KlAfmetingsensorType",
                         label="Afmetingsensor type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfmetingsensorType",
                         definition="Het type van de afmetingsensor.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfmetingsensorType")

        self.add_option("2D-LIDAR", "2D-LIDAR", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfmetingsensorType/2D-LIDAR")
        self.add_option("radar", "radar", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfmetingsensorType/radar")
        self.add_option("lussen-en-laserogen", "lussen en laserogen", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfmetingsensorType/lussen-en-laserogen")
