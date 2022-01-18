# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLETrottoirbandWatergreppelType(KeuzelijstField):
    """De vormen van een trottoirband_watergreppel."""
    naam = 'KlLETrottoirbandWatergreppelType'
    label = 'Trottoirband watergreppel type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLETrottoirbandWatergreppelType'
    definition = 'De vormen van een trottoirband_watergreppel.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLETrottoirbandWatergreppelType'
    options = {
        'type-III-A': KeuzelijstWaarde(invulwaarde='type-III-A',
                                       label='type III A',
                                       definitie='type III A',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandWatergreppelType/type-III-A'),
        'type-III-B': KeuzelijstWaarde(invulwaarde='type-III-B',
                                       label='type III B',
                                       definitie='type III B',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandWatergreppelType/type-III-B'),
        'type-III-C': KeuzelijstWaarde(invulwaarde='type-III-C',
                                       label='type III C',
                                       definitie='type III C',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandWatergreppelType/type-III-C'),
        'type-III-D': KeuzelijstWaarde(invulwaarde='type-III-D',
                                       label='type III D',
                                       definitie='type III D',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandWatergreppelType/type-III-D'),
        'type-III-E': KeuzelijstWaarde(invulwaarde='type-III-E',
                                       label='type III E',
                                       definitie='type III E',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandWatergreppelType/type-III-E')
    }

