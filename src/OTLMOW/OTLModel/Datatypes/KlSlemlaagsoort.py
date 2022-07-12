# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSlemlaagsoort(KeuzelijstField):
    """Soorten van slemlaag."""
    naam = 'KlSlemlaagsoort'
    label = 'Slemlaagsoort'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSlemlaagsoort'
    definition = 'Soorten van slemlaag.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSlemlaagsoort'
    options = {
        '0-10': KeuzelijstWaarde(invulwaarde='0-10',
                                 label='0/10',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='0/10',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemlaagsoort/0-10'),
        '0-2': KeuzelijstWaarde(invulwaarde='0-2',
                                label='0/2',
                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='0/2',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemlaagsoort/0-2'),
        '0-4': KeuzelijstWaarde(invulwaarde='0-4',
                                label='0/4',
                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='0/4',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemlaagsoort/0-4'),
        '0-6.3': KeuzelijstWaarde(invulwaarde='0-6.3',
                                  label='0/6.3',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='0/6,3',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemlaagsoort/0-6.3')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlSlemlaagsoort.get_dummy_data()

