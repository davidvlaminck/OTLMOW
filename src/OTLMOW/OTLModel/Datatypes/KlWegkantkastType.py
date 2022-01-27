# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWegkantkastType(KeuzelijstField):
    """Keuzelijst voor gangbare types voor wegkantkasten."""
    naam = 'KlWegkantkastType'
    label = 'Wegkantkast type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWegkantkastType'
    definition = 'Keuzelijst voor gangbare types voor wegkantkasten.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWegkantkastType'
    options = {
        'A': KeuzelijstWaarde(invulwaarde='A',
                              label='A',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegkantkastType/A'),
        'D': KeuzelijstWaarde(invulwaarde='D',
                              label='D',
                              definitie='Wegkantkast type D',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegkantkastType/D'),
        'DD': KeuzelijstWaarde(invulwaarde='DD',
                               label='DD',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegkantkastType/DD'),
        'E': KeuzelijstWaarde(invulwaarde='E',
                              label='E',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegkantkastType/E'),
        'F': KeuzelijstWaarde(invulwaarde='F',
                              label='F',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegkantkastType/F')
    }

