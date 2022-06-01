# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeerslichtMerk(KeuzelijstField):
    """Keuzelijst met merknamen voor Verkeerslicht."""
    naam = 'KlVerkeerslichtMerk'
    label = 'verkeerslicht merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerkeerslichtMerk'
    definition = 'Keuzelijst met merknamen voor Verkeerslicht.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeerslichtMerk'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlVerkeerslichtMerk.get_dummy_data()

