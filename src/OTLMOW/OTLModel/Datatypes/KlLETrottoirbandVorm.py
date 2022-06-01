# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLETrottoirbandVorm(KeuzelijstField):
    """De vormen van een trottoirband."""
    naam = 'KlLETrottoirbandVorm'
    label = 'Trottoirband vorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLETrottoirbandVorm'
    definition = 'De vormen van een trottoirband.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLETrottoirbandVorm'
    options = {
        'afgeschuind': KeuzelijstWaarde(invulwaarde='afgeschuind',
                                        label='afgeschuind',
                                        definitie='Afgeschuind',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandVorm/afgeschuind')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlLETrottoirbandVorm.get_dummy_data()

