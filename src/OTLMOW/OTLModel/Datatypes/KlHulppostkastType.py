# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHulppostkastType(KeuzelijstField):
    """Lijst met al dan niet gestandaardiseerde types voor hulppostkasten."""
    naam = 'KlHulppostkastType'
    label = 'Hulppostkast type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHulppostkastType'
    definition = 'Lijst met al dan niet gestandaardiseerde types voor hulppostkasten.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHulppostkastType'
    options = {
        'a': KeuzelijstWaarde(invulwaarde='a',
                              label='a',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulppostkastType/a'),
        'c': KeuzelijstWaarde(invulwaarde='c',
                              label='c',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulppostkastType/c')
    }

