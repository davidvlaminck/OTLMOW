# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeerslichtModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor Verkeerslicht."""
    naam = 'KlVerkeerslichtModelnaam'
    label = 'verkeerslicht modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerkeerslichtModelnaam'
    definition = 'Keuzelijst met modelnamen voor Verkeerslicht.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeerslichtModelnaam'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlVerkeerslichtModelnaam.get_dummy_data()

