# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKwaliteitsklasseHout(KeuzelijstField):
    """De kwaliteitsindeling van hout met betrekking op vervormingen, scheuren en kwasten."""
    naam = 'KlKwaliteitsklasseHout'
    label = 'Kwaliteitsklasse van hout'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlKwaliteitsklasseHout'
    definition = 'De kwaliteitsindeling van hout met betrekking op vervormingen, scheuren en kwasten.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKwaliteitsklasseHout'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlKwaliteitsklasseHout.get_dummy_data()

