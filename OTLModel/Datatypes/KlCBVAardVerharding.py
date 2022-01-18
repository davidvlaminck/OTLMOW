# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


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

