# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVirtueleServerMerk(KeuzelijstField):
    """Het merk van de virtuele server."""
    naam = 'KlVirtueleServerMerk'
    label = 'Virtuele server merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVirtueleServerMerk'
    definition = 'Het merk van de virtuele server.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVirtueleServerMerk'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlVirtueleServerMerk.get_dummy_data()

