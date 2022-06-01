# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCBVAardVerharding(KeuzelijstField):
    """Mogelijke waarden voor de aard van de cement/beton verharding."""
    naam = 'KlCBVAardVerharding'
    label = 'CBV aard verharding'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCBVAardVerharding'
    definition = 'Mogelijke waarden voor de aard van de cement/beton verharding.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCBVAardVerharding'
    options = {
        'doorgaand-gewapend-beton': KeuzelijstWaarde(invulwaarde='doorgaand-gewapend-beton',
                                                     label='doorgaand gewapend beton',
                                                     definitie='Verharding van doorgaand gewapend beton.',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVAardVerharding/doorgaand-gewapend-beton'),
        'gewapend-beton': KeuzelijstWaarde(invulwaarde='gewapend-beton',
                                           label='gewapend beton',
                                           definitie='Verharding van gewapend beton.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVAardVerharding/gewapend-beton'),
        'ongewapend-beton': KeuzelijstWaarde(invulwaarde='ongewapend-beton',
                                             label='ongewapend beton',
                                             definitie='Verharding van ongewapend beton.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVAardVerharding/ongewapend-beton'),
        'staalvezelbeton': KeuzelijstWaarde(invulwaarde='staalvezelbeton',
                                            label='staalvezelbeton',
                                            definitie='Verharding van staalvezelbeton.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVAardVerharding/staalvezelbeton')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlCBVAardVerharding.get_dummy_data()

