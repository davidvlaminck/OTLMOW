# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAudioversterkerModelnaam(KeuzelijstField):
    """De modelnaam van de audioversterker."""
    naam = 'KlAudioversterkerModelnaam'
    label = 'Audioversterker modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAudioversterkerModelnaam'
    definition = 'De modelnaam van de audioversterker.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAudioversterkerModelnaam'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlAudioversterkerModelnaam.get_dummy_data()

