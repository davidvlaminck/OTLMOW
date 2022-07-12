# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRepeaterMerk(KeuzelijstField):
    """Keuzelijst met merknamen voor Repeater."""
    naam = 'KlRepeaterMerk'
    label = 'repeater merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRepeaterMerk'
    definition = 'Keuzelijst met merknamen voor Repeater.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRepeaterMerk'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlRepeaterMerk.get_dummy_data()

