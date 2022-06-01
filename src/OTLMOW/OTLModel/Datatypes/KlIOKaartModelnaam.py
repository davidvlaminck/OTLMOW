# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIOKaartModelnaam(KeuzelijstField):
    """Lijst van mogelijke modelnamen voor IO-kaarten."""
    naam = 'KlIOKaartModelnaam'
    label = 'IO-kaart modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIOKaartModelnaam'
    definition = 'Lijst van mogelijke modelnamen voor IO-kaarten.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIOKaartModelnaam'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlIOKaartModelnaam.get_dummy_data()

