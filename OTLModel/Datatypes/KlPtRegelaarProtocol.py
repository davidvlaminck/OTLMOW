# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


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
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPtRegelaarProtocol/R0916'),
        'R0918': KeuzelijstWaarde(invulwaarde='R0918',
                                  label='R0918',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPtRegelaarProtocol/R0918')
    }

