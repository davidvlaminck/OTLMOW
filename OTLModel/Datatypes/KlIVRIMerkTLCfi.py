# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIMerkTLCfi(Keuzelijst):
    """Het merk van de TLC-fi poort."""

    def __init__(self):
        super().__init__(naam="KlIVRIMerkTLCfi",
                         label="iVRIMerkTLCfi",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIVRIMerkTLCfi",
                         definition="Het merk van de TLC-fi poort.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIMerkTLCfi")

        self.add_option("dynniq", "Dynniq", "Dynniq", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIMerkTLCfi/dynniq")
        self.add_option("ko-hartog", "Ko Hartog", "Ko Hartog", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIMerkTLCfi/ko-hartog")
        self.add_option("siemens", "Siemens", "Siemens", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIMerkTLCfi/siemens")
