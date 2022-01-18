# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersbordCode(KeuzelijstField):
    """De code van het verkeersbord volgens de wegcode."""
    naam = 'KlVerkeersbordCode'
    label = 'Verkeersbordcode'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersbordCode'
    definition = 'De code van het verkeersbord volgens de wegcode.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersbordCode'
    options = {
        'F34b1': KeuzelijstWaarde(invulwaarde='F34b1',
                                  label='F34b1',
                                  definitie='F34b1',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCode/F34b1'),
        'F34b2': KeuzelijstWaarde(invulwaarde='F34b2',
                                  label='F34b2',
                                  definitie='F34b2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCode/F34b2'),
        'F34c': KeuzelijstWaarde(invulwaarde='F34c',
                                 label='F34c',
                                 definitie='F34c',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCode/F34c'),
        'F35': KeuzelijstWaarde(invulwaarde='F35',
                                label='F35',
                                definitie='F35',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCode/F35'),
        'F37': KeuzelijstWaarde(invulwaarde='F37',
                                label='F37',
                                definitie='F37',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCode/F37'),
        'F67': KeuzelijstWaarde(invulwaarde='F67',
                                label='F67',
                                definitie='F67',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCode/F67')
    }

