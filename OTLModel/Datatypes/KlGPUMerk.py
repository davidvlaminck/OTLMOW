# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGPUMerk(Keuzelijst):
    """Het merk van de GPU."""

    def __init__(self):
        super().__init__(naam="KlGPUMerk",
                         label="GPU merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGPUMerk",
                         definition="Het merk van de GPU.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGPUMerk")

        self.add_option("nvidia", "Nvidia", "Nvidia", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGPUMerk/nvidia")
