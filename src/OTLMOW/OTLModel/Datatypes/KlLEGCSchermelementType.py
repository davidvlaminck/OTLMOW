# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCSchermelementType(KeuzelijstField):
    """Schermelement types."""
    naam = 'KlLEGCSchermelementType'
    label = 'Schermelement type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCSchermelementType'
    definition = 'Schermelement types.'
    deprecated_version = '2.0.0'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCSchermelementType'
    options = {
        'bloembakelement': KeuzelijstWaarde(invulwaarde='bloembakelement',
                                            label='bloembakelement',
                                            definitie='bloembakelement',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCSchermelementType/bloembakelement'),
        'l-element': KeuzelijstWaarde(invulwaarde='l-element',
                                      label='l-element',
                                      definitie='l-element',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCSchermelementType/l-element'),
        'schermelement-tussen-palen': KeuzelijstWaarde(invulwaarde='schermelement-tussen-palen',
                                                       label='schermelement tussen palen',
                                                       definitie='schermelement tussen palen',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCSchermelementType/schermelement-tussen-palen'),
        'voertuigkerend': KeuzelijstWaarde(invulwaarde='voertuigkerend',
                                           label='voertuigkerend',
                                           definitie='voertuigkerend',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCSchermelementType/voertuigkerend')
    }

