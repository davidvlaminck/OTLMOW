# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPCIkaartMerk(KeuzelijstField):
    """Het merk van de PCI-kaart."""
    naam = 'KlPCIkaartMerk'
    label = 'PCI-kaart merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPCIkaartMerk'
    definition = 'Het merk van de PCI-kaart.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPCIkaartMerk'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlPCIkaartMerk.get_dummy_data()

