# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAudioTransportType(Keuzelijst):
    """Lijst met mogelijke types voor transport van audio over een medium."""

    def __init__(self):
        super().__init__(naam="KlAudioTransportType",
                         label="Audio transport type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAudioTransportType",
                         definition="Lijst met mogelijke types voor transport van audio over een medium.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAudioTransportType")

        self.add_option("analoog", "analoog", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAudioTransportType/analoog")
        self.add_option("voip", "voip", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAudioTransportType/voip")
