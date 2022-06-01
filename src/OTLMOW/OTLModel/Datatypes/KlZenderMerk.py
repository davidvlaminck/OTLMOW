# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZenderMerk(KeuzelijstField):
    """Keuzelijst met merknamen voor Zender."""
    naam = 'KlZenderMerk'
    label = 'zender merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlZenderMerk'
    definition = 'Keuzelijst met merknamen voor Zender.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZenderMerk'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlZenderMerk.get_dummy_data()

