# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIModelITSapp(KeuzelijstField):
    """De modelnaam van de ITSapp."""
    naam = 'KlIVRIModelITSapp'
    label = 'iVRIModelITSapp'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIVRIModelITSapp'
    definition = 'De modelnaam van de ITSapp.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIModelITSapp'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlIVRIModelITSapp.get_dummy_data()

