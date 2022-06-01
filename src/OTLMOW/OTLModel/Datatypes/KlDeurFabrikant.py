# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDeurFabrikant(KeuzelijstField):
    """Lijst van fabrikanten van deuren."""
    naam = 'KlDeurFabrikant'
    label = 'Deur fabrikant'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlDeurFabrikant'
    definition = 'Lijst van fabrikanten van deuren.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDeurFabrikant'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlDeurFabrikant.get_dummy_data()

