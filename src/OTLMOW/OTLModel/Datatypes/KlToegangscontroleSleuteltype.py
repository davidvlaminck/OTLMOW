# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlToegangscontroleSleuteltype(KeuzelijstField):
    """Types voor sleutels die toegang geven tot een behuizing."""
    naam = 'KlToegangscontroleSleuteltype'
    label = 'Toegangscontrole sleuteltype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlToegangscontroleSleuteltype'
    definition = 'Types voor sleutels die toegang geven tot een behuizing.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlToegangscontroleSleuteltype'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlToegangscontroleSleuteltype.get_dummy_data()

