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
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSlemlaagsoort'
    options = {
        '0-10': KeuzelijstWaarde(invulwaarde='0-10',
                                 label='0/10',
                                 status='ingebruik',
                                 definitie='0/10',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemlaagsoort/0-10'),
        '0-2': KeuzelijstWaarde(invulwaarde='0-2',
                                label='0/2',
                                status='ingebruik',
                                definitie='0/2',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemlaagsoort/0-2'),
        '0-4': KeuzelijstWaarde(invulwaarde='0-4',
                                label='0/4',
                                status='ingebruik',
                                definitie='0/4',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemlaagsoort/0-4'),
        '0-6.3': KeuzelijstWaarde(invulwaarde='0-6.3',
                                  label='0/6.3',
                                  status='ingebruik',
                                  definitie='0/6,3',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemlaagsoort/0-6.3')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

