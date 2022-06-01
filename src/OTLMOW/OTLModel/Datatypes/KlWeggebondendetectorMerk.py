# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWeggebondendetectorMerk(KeuzelijstField):
    """Keuzelijst met merknamen voor Weggebondendetector."""
    naam = 'KlWeggebondendetectorMerk'
    label = 'Weggebondendetector merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeggebondendetectorMerk'
    definition = 'Keuzelijst met merknamen voor Weggebondendetector.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeggebondendetectorMerk'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlWeggebondendetectorMerk.get_dummy_data()

