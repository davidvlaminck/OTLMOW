# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCADOModelnaam(KeuzelijstField):
    """De modelnaam van de calamiteitendoorsteek."""
    naam = 'KlCADOModelnaam'
    label = 'Calamiteitendoorsteek modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCADOModelnaam'
    definition = 'De modelnaam van de calamiteitendoorsteek.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCADOModelnaam'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlCADOModelnaam.get_dummy_data()

