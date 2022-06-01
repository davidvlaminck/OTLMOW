# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVariabelDeelType(KeuzelijstField):
    """Types van het variabel deel van een overstortrand."""
    naam = 'KlVariabelDeelType'
    label = 'Variabel deel type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVariabelDeelType'
    definition = 'Types van het variabel deel van een overstortrand.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVariabelDeelType'
    options = {
        'overstortplaat': KeuzelijstWaarde(invulwaarde='overstortplaat',
                                           label='overstortplaat',
                                           definitie='overstortplaat',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVariabelDeelType/overstortplaat'),
        'schotbalk': KeuzelijstWaarde(invulwaarde='schotbalk',
                                      label='schotbalk',
                                      definitie='schotbalk',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVariabelDeelType/schotbalk')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlVariabelDeelType.get_dummy_data()

