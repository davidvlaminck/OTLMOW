# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerwarmingselementMerk(KeuzelijstField):
    """Keuzelijst van merken voor verwarmingselementen."""
    naam = 'KlVerwarmingselementMerk'
    label = 'Verwarmingselement merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerwarmingselementMerk'
    definition = 'Keuzelijst van merken voor verwarmingselementen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerwarmingselementMerk'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlVerwarmingselementMerk.get_dummy_data()

