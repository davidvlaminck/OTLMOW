# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEDDriverModelnaam(KeuzelijstField):
    """De modelnaam van de LED-driver."""
    naam = 'KlLEDDriverModelnaam'
    label = 'LED-driver modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEDDriverModelnaam'
    definition = 'De modelnaam van de LED-driver.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEDDriverModelnaam'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlLEDDriverModelnaam.get_dummy_data()

