# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIntercomServerModelnaam(KeuzelijstField):
    """De modelnaam van de intercomserver."""
    naam = 'KlIntercomServerModelnaam'
    label = 'Intercomserver modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIntercomServerModelnaam'
    definition = 'De modelnaam van de intercomserver.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIntercomServerModelnaam'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlIntercomServerModelnaam.get_dummy_data()

