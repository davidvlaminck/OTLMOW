# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAudioversterkerMerk(Keuzelijst):
    """Het merk van de audioversterker."""

    def __init__(self):
        super().__init__(naam="KlAudioversterkerMerk",
                         label="Audioversterker merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAudioversterkerMerk",
                         definition="Het merk van de audioversterker.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAudioversterkerMerk")

