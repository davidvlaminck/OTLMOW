# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class AntiParkeerpaalType(KeuzelijstField):
    """De vormen van een anti-parkeerpaal."""
    naam = 'AntiParkeerpaalType'
    label = 'Anti-parkeerpaal type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AntiParkeerpaalType'
    definition = 'De vormen van een anti-parkeerpaal.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/AntiParkeerpaalType'
    options = {
        'conischeTrottoirpaalAmsterdammer': KeuzelijstWaarde(invulwaarde='conischeTrottoirpaalAmsterdammer',
                                                             label='conischeTrottoirpaalAmsterdammer',
                                                             definitie='Conische paal met afgeronde kop en sierring.',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/AntiParkeerpaalType/conischeTrottoirpaalAmsterdammer'),
        'diamantkoppaal': KeuzelijstWaarde(invulwaarde='diamantkoppaal',
                                           label='diamantkoppaal',
                                           definitie='Een paal voorzien van een diamantkop en op de hoeken 4 vellingkanten.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/AntiParkeerpaalType/diamantkoppaal')
    }

