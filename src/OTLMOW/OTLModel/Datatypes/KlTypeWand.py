# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeWand(KeuzelijstField):
    """Keuzelijst met modelnamen voor KlTypeWand."""
    naam = 'KlTypeWand'
    label = 'Batterij CU modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeWand'
    definition = 'Keuzelijst met modelnamen voor VRBatterijCU.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeWand'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlTypeWand.get_dummy_data()

