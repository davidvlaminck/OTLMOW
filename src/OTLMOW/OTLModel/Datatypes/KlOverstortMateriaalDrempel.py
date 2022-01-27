# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOverstortMateriaalDrempel(KeuzelijstField):
    """De materialen van vervaardiging van de overstort."""
    naam = 'KlOverstortMateriaalDrempel'
    label = 'Overstort materiaal drempel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOverstortMateriaalDrempel'
    definition = 'De materialen van vervaardiging van de overstort.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOverstortMateriaalDrempel'
    options = {
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  definitie='beton',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverstortMateriaalDrempel/beton'),
        'metselwerk': KeuzelijstWaarde(invulwaarde='metselwerk',
                                       label='metselwerk',
                                       definitie='metselwerk',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverstortMateriaalDrempel/metselwerk')
    }

