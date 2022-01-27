# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVegetatiePlantverband(KeuzelijstField):
    """De verschillende opties voor het plantverband."""
    naam = 'KlVegetatiePlantverband'
    label = 'Vegetatie plantverband'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVegetatiePlantverband'
    definition = 'De verschillende opties voor het plantverband.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVegetatiePlantverband'
    options = {
        'geschrankt': KeuzelijstWaarde(invulwaarde='geschrankt',
                                       label='geschrankt',
                                       definitie='De planten staan geschrankt',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatiePlantverband/geschrankt'),
        'rijafstand': KeuzelijstWaarde(invulwaarde='rijafstand',
                                       label='rijafstand',
                                       definitie='De afstand tussen de rijen',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatiePlantverband/rijafstand')
    }

