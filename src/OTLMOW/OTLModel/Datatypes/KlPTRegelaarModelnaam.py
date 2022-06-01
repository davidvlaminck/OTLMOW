# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPTRegelaarModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor PTRegelaar."""
    naam = 'KlPTRegelaarModelnaam'
    label = 'PT regelaar modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPTRegelaarModelnaam'
    definition = 'Keuzelijst met modelnamen voor PTRegelaar.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPTRegelaarModelnaam'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlPTRegelaarModelnaam.get_dummy_data()

