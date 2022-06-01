# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIMerkRIS(KeuzelijstField):
    """Het merk van de RIS."""
    naam = 'KlIVRIMerkRIS'
    label = 'iVRIMerkRIS'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIVRIMerkRIS'
    definition = 'Het merk van de RIS.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIMerkRIS'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlIVRIMerkRIS.get_dummy_data()

