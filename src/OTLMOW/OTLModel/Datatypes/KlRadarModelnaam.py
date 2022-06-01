# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRadarModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor Radar."""
    naam = 'KlRadarModelnaam'
    label = 'Radar modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRadarModelnaam'
    definition = 'Keuzelijst met modelnamen voor Radar.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRadarModelnaam'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlRadarModelnaam.get_dummy_data()

