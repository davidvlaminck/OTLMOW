# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDuurzaamheidsklasseHout(KeuzelijstField):
    """De resistentie van het kernhout tegen ongunstige omstandigheden."""
    naam = 'KlDuurzaamheidsklasseHout'
    label = 'Duurzaamheidsklasse van hout'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlDuurzaamheidsklasseHout'
    definition = 'De resistentie van het kernhout tegen ongunstige omstandigheden.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDuurzaamheidsklasseHout'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlDuurzaamheidsklasseHout.get_dummy_data()

