# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSchoorhoek(KeuzelijstField):
    """De schoorhoek van het object, uitgedrukt in 1 op x (vb.: 1/4)."""
    naam = 'KlSchoorhoek'
    label = 'Schoorhoek'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlSchoorhoek'
    definition = 'De schoorhoek van het object, uitgedrukt in 1 op x (vb.: 1/4).'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSchoorhoek'
    options = {
        '1-3': KeuzelijstWaarde(invulwaarde='1-3',
                                label='1/3',
                                definitie='Een schoorhoek van 1 op 3.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchoorhoek/1-3'),
        '1-4': KeuzelijstWaarde(invulwaarde='1-4',
                                label='1/4',
                                definitie='Een schoorhoek van 1 op 4.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchoorhoek/1-4')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlSchoorhoek.get_dummy_data()

