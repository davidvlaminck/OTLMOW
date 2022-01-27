# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVegetatieDrassigheid(KeuzelijstField):
    """De mate van drassigheid.."""
    naam = 'KlVegetatieDrassigheid'
    label = 'Vegetatie drassigheid'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVegetatieDrassigheid'
    definition = 'De mate van drassigheid..'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVegetatieDrassigheid'
    options = {
        'matig-drassig': KeuzelijstWaarde(invulwaarde='matig-drassig',
                                          label='matig drassig',
                                          definitie='De ondergrond is matig drassig',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieDrassigheid/matig-drassig'),
        'niet-drassig': KeuzelijstWaarde(invulwaarde='niet-drassig',
                                         label='niet drassig',
                                         definitie='De ondergrond is niet drassig',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieDrassigheid/niet-drassig'),
        'sterk-drassig': KeuzelijstWaarde(invulwaarde='sterk-drassig',
                                          label='sterk drassig',
                                          definitie='De ondergrond is sterk drassig',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieDrassigheid/sterk-drassig')
    }

