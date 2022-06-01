# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFietstelsysteemModelnaam(KeuzelijstField):
    """Lijst met mogelijke modelnamen voor fietstelsystemen."""
    naam = 'KlFietstelsysteemModelnaam'
    label = 'Modelnaam fietstelsysteem'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFietstelsysteemModelnaam'
    definition = 'Lijst met mogelijke modelnamen voor fietstelsystemen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFietstelsysteemModelnaam'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlFietstelsysteemModelnaam.get_dummy_data()

