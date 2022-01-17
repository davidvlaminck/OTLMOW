# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRasterMazen(KeuzelijstField):
    """Types van de mazen in het ecoraster."""
    naam = 'KlRasterMazen'
    label = 'Rastermazen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRasterMazen'
    definition = 'Types van de mazen in het ecoraster.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRasterMazen'
    options = {
        'fijnmazig': KeuzelijstWaarde(invulwaarde='fijnmazig',
                                      label='fijnmazig',
                                      definitie='Een fijnmazig raster.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRasterMazen/fijnmazig'),
        'grofmazig': KeuzelijstWaarde(invulwaarde='grofmazig',
                                      label='grofmazig',
                                      definitie='Een grofmazig raster.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRasterMazen/grofmazig')
    }

