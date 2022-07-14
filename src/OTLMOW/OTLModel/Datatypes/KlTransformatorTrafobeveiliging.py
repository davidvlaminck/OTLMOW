# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTransformatorTrafobeveiliging(KeuzelijstField):
    """Type transformatorbeveiliging."""
    naam = 'KlTransformatorTrafobeveiliging'
    label = 'Transformator trafobeveiliging'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTransformatorTrafobeveiliging'
    definition = 'Type transformatorbeveiliging.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTransformatorTrafobeveiliging'
    options = {
        'gecombineerd': KeuzelijstWaarde(invulwaarde='gecombineerd',
                                         label='gecombineerd',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorTrafobeveiliging/gecombineerd'),
        'overdruk': KeuzelijstWaarde(invulwaarde='overdruk',
                                     label='overdruk',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorTrafobeveiliging/overdruk'),
        'overtemperatuur': KeuzelijstWaarde(invulwaarde='overtemperatuur',
                                            label='overtemperatuur',
                                            status='ingebruik',
                                            definitie='attributen invullen//',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorTrafobeveiliging/overtemperatuur')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

