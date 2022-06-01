# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACSchokindex(KeuzelijstField):
    """De verschillende schokindices."""
    naam = 'KlLEACSchokindex'
    label = 'Schokindex'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACSchokindex'
    definition = 'De verschillende schokindices.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACSchokindex'
    options = {
        'a': KeuzelijstWaarde(invulwaarde='a',
                              label='a',
                              definitie='ASI <= 1.0 (zeer veilig)',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACSchokindex/a'),
        'b': KeuzelijstWaarde(invulwaarde='b',
                              label='b',
                              definitie='ASI <= 1.4 (voldoende veilig)',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACSchokindex/b'),
        'c': KeuzelijstWaarde(invulwaarde='c',
                              label='c',
                              definitie='ASI <= 1.9',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACSchokindex/c')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlLEACSchokindex.get_dummy_data()

