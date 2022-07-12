# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersbordCode(KeuzelijstField):
    """De code van het verkeersbord volgens de wegcode."""
    naam = 'KlVerkeersbordCode'
    label = 'Verkeersbordcode'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersbordCode'
    definition = 'De code van het verkeersbord volgens de wegcode.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersbordCode'
    options = {
        'F34b1': KeuzelijstWaarde(invulwaarde='F34b1',
                                  label='F34b1',
                                  status='ingebruik',
                                  definitie='F34b1',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCode/F34b1'),
        'F34b2': KeuzelijstWaarde(invulwaarde='F34b2',
                                  label='F34b2',
                                  status='ingebruik',
                                  definitie='F34b2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCode/F34b2'),
        'F34c': KeuzelijstWaarde(invulwaarde='F34c',
                                 label='F34c',
                                 status='ingebruik',
                                 definitie='F34c',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCode/F34c'),
        'F35': KeuzelijstWaarde(invulwaarde='F35',
                                label='F35',
                                status='ingebruik',
                                definitie='F35',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCode/F35'),
        'F37': KeuzelijstWaarde(invulwaarde='F37',
                                label='F37',
                                status='ingebruik',
                                definitie='F37',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCode/F37'),
        'F67': KeuzelijstWaarde(invulwaarde='F67',
                                label='F67',
                                status='ingebruik',
                                definitie='F67',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCode/F67')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlVerkeersbordCode.get_dummy_data()

