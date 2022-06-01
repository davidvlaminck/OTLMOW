# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeUitkraging(KeuzelijstField):
    """Beschrijft het protocol waarmee de PT-regelaar communiceert."""
    naam = 'KlPtRegelaarProtocol'
    label = 'PT-regelaar protocol'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPtRegelaarProtocol'
    definition = 'Beschrijft het protocol waarmee de PT-regelaar communiceert.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPtRegelaarProtocol'
    options = {}

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlTypeUitkraging.get_dummy_data()

