# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeVakwerkElement(KeuzelijstField):
    """Bepaling van het vervaardigingsmateriaal van de antiparkeerpaal."""
    naam = 'KlAntiparkeerpaalMateriaal'
    label = 'Antiparkeerpaal materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAntiparkeerpaalMateriaal'
    definition = 'Bepaling van het vervaardigingsmateriaal van de antiparkeerpaal.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAntiparkeerpaalMateriaal'
    options = {}

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlTypeVakwerkElement.get_dummy_data()

