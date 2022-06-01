# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHSBeveiligingscelModelnaam(KeuzelijstField):
    """De modelnaam van de HS-beveiligingscel."""
    naam = 'KlHSBeveiligingscelModelnaam'
    label = 'HS-beveiligingscel modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHSBeveiligingscelModelnaam'
    definition = 'De modelnaam van de HS-beveiligingscel.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHSBeveiligingscelModelnaam'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlHSBeveiligingscelModelnaam.get_dummy_data()

