# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCSchermelementType(KeuzelijstField):
    """Schermelement types."""
    naam = 'KlLEGCSchermelementType'
    label = 'Schermelement type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCSchermelementType'
    definition = 'Schermelement types.'
    status = 'ingebruik'
    deprecated_version = '2.0.0'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCSchermelementType'
    options = {
        'bloembakelement': KeuzelijstWaarde(invulwaarde='bloembakelement',
                                            label='bloembakelement',
                                            status='ingebruik',
                                            definitie='bloembakelement',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCSchermelementType/bloembakelement'),
        'l-element': KeuzelijstWaarde(invulwaarde='l-element',
                                      label='l-element',
                                      status='ingebruik',
                                      definitie='l-element',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCSchermelementType/l-element'),
        'schermelement-tussen-palen': KeuzelijstWaarde(invulwaarde='schermelement-tussen-palen',
                                                       label='schermelement tussen palen',
                                                       status='ingebruik',
                                                       definitie='schermelement tussen palen',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCSchermelementType/schermelement-tussen-palen'),
        'voertuigkerend': KeuzelijstWaarde(invulwaarde='voertuigkerend',
                                           label='voertuigkerend',
                                           status='ingebruik',
                                           definitie='voertuigkerend',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCSchermelementType/voertuigkerend')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

