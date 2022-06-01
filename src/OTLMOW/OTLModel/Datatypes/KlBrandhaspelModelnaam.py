# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBrandhaspelModelnaam(KeuzelijstField):
    """De modelnaam van de brandhaspel."""
    naam = 'KlBrandhaspelModelnaam'
    label = 'brandhaspel model naam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBrandhaspelModelnaam'
    definition = 'De modelnaam van de brandhaspel.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBrandhaspelModelnaam'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBrandhaspelModelnaam.get_dummy_data()

