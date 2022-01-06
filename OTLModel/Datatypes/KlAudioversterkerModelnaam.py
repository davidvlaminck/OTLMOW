# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAudioversterkerModelnaam(Keuzelijst):
    """De modelnaam van de audioversterker."""

    def __init__(self):
        super().__init__(naam="KlAudioversterkerModelnaam",
                         label="Audioversterker modelnaam",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAudioversterkerModelnaam",
                         definition="De modelnaam van de audioversterker.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAudioversterkerModelnaam")

