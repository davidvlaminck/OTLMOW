# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeFlitspaal(KeuzelijstField):
    """De mogelijke types van flitspalen gebruikt in een zone."""
    naam = 'KlTypeFlitspaal'
    label = 'Types flitspalen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeFlitspaal'
    definition = 'De mogelijke types van flitspalen gebruikt in een zone.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeFlitspaal'
    options = {
        'analoog-en-digitaal': KeuzelijstWaarde(invulwaarde='analoog-en-digitaal',
                                      label='Analoog en digitaal',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/analoog-en-digitaal'),
        'hybride-en-digitaal': KeuzelijstWaarde(invulwaarde='hybride-en-digitaal',
                                  label='Hybride en digitaal',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/hybride-en-digitaal'),
        'digitaal': KeuzelijstWaarde(invulwaarde='digitaal',
                                 label='Digitaal',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/digitaal'),
    }

