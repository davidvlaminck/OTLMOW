# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGeotextielType(KeuzelijstField):
    """Types van geotextiel."""
    naam = 'KlGeotextielType'
    label = 'Geotextiel type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGeotextielType'
    definition = 'Types van geotextiel.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGeotextielType'
    options = {
        'anti-vraatdoek': KeuzelijstWaarde(invulwaarde='anti-vraatdoek',
                                           label='anti-vraatdoek',
                                           definitie='anti-vraatdoek',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeotextielType/anti-vraatdoek'),
        'bescherming': KeuzelijstWaarde(invulwaarde='bescherming',
                                        label='bescherming',
                                        definitie='bescherming/wapening',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeotextielType/bescherming'),
        'erosiewerend': KeuzelijstWaarde(invulwaarde='erosiewerend',
                                         label='erosiewerend',
                                         definitie='erosiewerend',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeotextielType/erosiewerend'),
        'niet-geweven-geotextiel': KeuzelijstWaarde(invulwaarde='niet-geweven-geotextiel',
                                                    label='niet-geweven geotextiel',
                                                    definitie='niet-geweven geotextiel',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeotextielType/niet-geweven-geotextiel'),
        'wapening': KeuzelijstWaarde(invulwaarde='wapening',
                                     label='wapening',
                                     definitie='bescherming/wapening',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeotextielType/wapening')
    }

