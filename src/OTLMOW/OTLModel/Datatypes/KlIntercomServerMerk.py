# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIntercomServerMerk(KeuzelijstField):
    """Het merk van de intercomserver."""
    naam = 'KlIntercomServerMerk'
    label = 'Intercomserver merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIntercomServerMerk'
    definition = 'Het merk van de intercomserver.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIntercomServerMerk'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlIntercomServerMerk.get_dummy_data()

