# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAudioTransportType(KeuzelijstField):
    """Lijst met mogelijke types voor transport van audio over een medium."""
    naam = 'KlAudioTransportType'
    label = 'Audio transport type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAudioTransportType'
    definition = 'Lijst met mogelijke types voor transport van audio over een medium.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAudioTransportType'
    options = {
        'analoog': KeuzelijstWaarde(invulwaarde='analoog',
                                    label='analoog',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAudioTransportType/analoog'),
        'voip': KeuzelijstWaarde(invulwaarde='voip',
                                 label='voip',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAudioTransportType/voip')
    }

