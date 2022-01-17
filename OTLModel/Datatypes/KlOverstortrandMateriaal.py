# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOverstortrandMateriaal(KeuzelijstField):
    """De materialen van de overstortrand."""
    naam = 'KlOverstortrandMateriaal'
    label = 'Overstortrand materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOverstortrandMateriaal'
    definition = 'De materialen van de overstortrand.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOverstortrandMateriaal'
    options = {
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='hout',
                                 definitie='Een overstortrand uit hout.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverstortrandMateriaal/hout'),
        'inox': KeuzelijstWaarde(invulwaarde='inox',
                                 label='inox',
                                 definitie='Een overstortrand uit inox.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverstortrandMateriaal/inox'),
        'metselwerk': KeuzelijstWaarde(invulwaarde='metselwerk',
                                       label='metselwerk',
                                       definitie='Een overstortrand uit metselwerk.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverstortrandMateriaal/metselwerk')
    }

