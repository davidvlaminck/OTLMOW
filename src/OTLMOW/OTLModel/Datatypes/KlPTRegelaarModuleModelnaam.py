# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPTRegelaarModuleModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor PTRegelaarModule."""
    naam = 'KlPTRegelaarModuleModelnaam'
    label = 'PT regelaarmodule modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlPTRegelaarModuleModelnaam'
    definition = 'Keuzelijst met modelnamen voor PTRegelaarModule.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPTRegelaarModuleModelnaam'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlPTRegelaarModuleModelnaam.get_dummy_data()

