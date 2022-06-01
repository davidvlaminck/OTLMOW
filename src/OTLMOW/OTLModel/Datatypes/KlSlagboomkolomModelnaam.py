# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSlagboomkolomModelnaam(KeuzelijstField):
    """De modelnaam van de slagboomkolom."""
    naam = 'KlSlagboomkolomModelnaam'
    label = 'Slagboomkolom modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSlagboomkolomModelnaam'
    definition = 'De modelnaam van de slagboomkolom.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSlagboomkolomModelnaam'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlSlagboomkolomModelnaam.get_dummy_data()

