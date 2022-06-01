# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCodeklavierMerk(KeuzelijstField):
    """Het merk van het codeklavier."""
    naam = 'KlCodeklavierMerk'
    label = 'Codeklavier merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCodeklavierMerk'
    definition = 'Het merk van het codeklavier.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCodeklavierMerk'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlCodeklavierMerk.get_dummy_data()

