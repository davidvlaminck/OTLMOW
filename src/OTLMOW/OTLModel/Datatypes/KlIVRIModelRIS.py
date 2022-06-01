# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIModelRIS(KeuzelijstField):
    """De modelnaam van de RIS."""
    naam = 'KlIVRIModelRIS'
    label = 'iVRIModelRIS'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIVRIModelRIS'
    definition = 'De modelnaam van de RIS.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIModelRIS'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlIVRIModelRIS.get_dummy_data()

