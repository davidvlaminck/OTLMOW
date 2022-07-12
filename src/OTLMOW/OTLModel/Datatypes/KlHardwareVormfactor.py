# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHardwareVormfactor(KeuzelijstField):
    """Het soort toestel waarin de fysieke componenten of onderdelen worden vormgegeven."""
    naam = 'KlHardwareVormfactor'
    label = 'Hardware vormfactor'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHardwareVormfactor'
    definition = 'Het soort toestel waarin de fysieke componenten of onderdelen worden vormgegeven.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHardwareVormfactor'
    options = {
        'desktop': KeuzelijstWaarde(invulwaarde='desktop',
                                    label='desktop',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareVormfactor/desktop'),
        'laptop': KeuzelijstWaarde(invulwaarde='laptop',
                                   label='laptop',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareVormfactor/laptop'),
        'server': KeuzelijstWaarde(invulwaarde='server',
                                   label='server',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareVormfactor/server')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlHardwareVormfactor.get_dummy_data()

