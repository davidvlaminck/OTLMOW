# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWIMDataloggerModelnaam(KeuzelijstField):
    """De modelnaam van de WIM-datalogger."""
    naam = 'KlWIMDataloggerModelnaam'
    label = 'WIM-datalogger modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWIMDataloggerModelnaam'
    definition = 'De modelnaam van de WIM-datalogger.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWIMDataloggerModelnaam'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlWIMDataloggerModelnaam.get_dummy_data()

