# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVirtueleServerModelnaam(KeuzelijstField):
    """De modelnaam van de virtuele server."""
    naam = 'KlVirtueleServerModelnaam'
    label = 'Virtuele server modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVirtueleServerModelnaam'
    definition = 'De modelnaam van de virtuele server.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVirtueleServerModelnaam'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlVirtueleServerModelnaam.get_dummy_data()

