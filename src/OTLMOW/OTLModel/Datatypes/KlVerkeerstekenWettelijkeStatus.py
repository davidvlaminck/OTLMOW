# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeerstekenWettelijkeStatus(KeuzelijstField):
    """Keuzelijst met waarden die de wettelijke status van een verkeersteken aangeven."""
    naam = 'KlVerkeerstekenWettelijkeStatus'
    label = 'VerkeerstekenWettelijkeStatus'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeerstekenWettelijkeStatus'
    definition = 'Keuzelijst met waarden die de wettelijke status van een verkeersteken aangeven.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeerstekenWettelijkeStatus'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlVerkeerstekenWettelijkeStatus.get_dummy_data()

