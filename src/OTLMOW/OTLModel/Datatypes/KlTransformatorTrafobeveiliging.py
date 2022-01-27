# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTransformatorTrafobeveiliging(KeuzelijstField):
    """Type transformatorbeveiliging."""
    naam = 'KlTransformatorTrafobeveiliging'
    label = 'Transformator trafobeveiliging'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTransformatorTrafobeveiliging'
    definition = 'Type transformatorbeveiliging.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTransformatorTrafobeveiliging'
    options = {
        'gecombineerd': KeuzelijstWaarde(invulwaarde='gecombineerd',
                                         label='gecombineerd',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorTrafobeveiliging/gecombineerd'),
        'overdruk': KeuzelijstWaarde(invulwaarde='overdruk',
                                     label='overdruk',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorTrafobeveiliging/overdruk'),
        'overtemperatuur': KeuzelijstWaarde(invulwaarde='overtemperatuur',
                                            label='overtemperatuur',
                                            definitie='attributen invullen//',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorTrafobeveiliging/overtemperatuur')
    }

