# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBGSchermelementtype(KeuzelijstField):
    """Het type bijzonder-schermelement."""
    naam = 'KlBGSchermelementtype'
    label = 'Bijzonder geluidsschermelementtype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBGSchermelementtype'
    definition = 'Het type bijzonder-schermelement.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBGSchermelementtype'
    options = {
        'bloembakelement': KeuzelijstWaarde(invulwaarde='bloembakelement',
                                            label='bloembakelement',
                                            definitie='bloembakelement',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBGSchermelementtype/bloembakelement'),
        'l-element': KeuzelijstWaarde(invulwaarde='l-element',
                                      label='L-element',
                                      definitie='L-element',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBGSchermelementtype/l-element')
    }

