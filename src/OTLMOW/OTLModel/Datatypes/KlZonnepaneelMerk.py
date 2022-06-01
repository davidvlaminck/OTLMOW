# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZonnepaneelMerk(KeuzelijstField):
    """Het merk van het zonnepaneel."""
    naam = 'KlZonnepaneelMerk'
    label = 'Zonnepaneel merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlZonnepaneelMerk'
    definition = 'Het merk van het zonnepaneel.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZonnepaneelMerk'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlZonnepaneelMerk.get_dummy_data()

