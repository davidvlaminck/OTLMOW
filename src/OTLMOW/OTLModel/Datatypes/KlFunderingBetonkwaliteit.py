# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFunderingBetonkwaliteit(KeuzelijstField):
    """Mogelijke waarden voor de betonkwaliteit van een fundering."""
    naam = 'KlFunderingBetonkwaliteit'
    label = 'Fundering betonkwaliteit'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFunderingBetonkwaliteit'
    definition = 'Mogelijke waarden voor de betonkwaliteit van een fundering.'
    deprecated_version = '2.0.0'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFunderingBetonkwaliteit'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlFunderingBetonkwaliteit.get_dummy_data()

