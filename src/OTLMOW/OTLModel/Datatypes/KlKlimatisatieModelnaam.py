# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKlimatisatieModelnaam(KeuzelijstField):
    """Modelnamen voor klimatisatiesystemen."""
    naam = 'KlKlimatisatieModelnaam'
    label = 'Klimatisatie modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKlimatisatieModelnaam'
    definition = 'Modelnamen voor klimatisatiesystemen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKlimatisatieModelnaam'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlKlimatisatieModelnaam.get_dummy_data()

