# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRadarMerk(KeuzelijstField):
    """Keuzelijst met merknamen voor Radar."""
    naam = 'KlRadarMerk'
    label = 'Radar merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRadarMerk'
    definition = 'Keuzelijst met merknamen voor Radar.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRadarMerk'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlRadarMerk.get_dummy_data()

