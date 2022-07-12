# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPtRegelaarProtocol(KeuzelijstField):
    """Beschrijft het protocol waarmee de PT-regelaar communiceert."""
    naam = 'KlPtRegelaarProtocol'
    label = 'PT-regelaar protocol'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPtRegelaarProtocol'
    definition = 'Beschrijft het protocol waarmee de PT-regelaar communiceert.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPtRegelaarProtocol'
    options = {
        'R0916': KeuzelijstWaarde(invulwaarde='R0916',
                                  label='R0916',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPtRegelaarProtocol/R0916'),
        'R0918': KeuzelijstWaarde(invulwaarde='R0918',
                                  label='R0918',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPtRegelaarProtocol/R0918')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlPtRegelaarProtocol.get_dummy_data()

