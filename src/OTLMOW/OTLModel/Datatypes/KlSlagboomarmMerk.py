# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSlagboomarmMerk(KeuzelijstField):
    """Het merk van de slagboomarm."""
    naam = 'KlSlagboomarmMerk'
    label = 'Slagboomarm merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSlagboomarmMerk'
    definition = 'Het merk van de slagboomarm.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSlagboomarmMerk'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlSlagboomarmMerk.get_dummy_data()

