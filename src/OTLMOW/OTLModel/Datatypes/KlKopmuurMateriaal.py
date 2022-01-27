# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKopmuurMateriaal(KeuzelijstField):
    """Materialen van de kopmuur."""
    naam = 'KlKopmuurMateriaal'
    label = 'Kopmuur materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKopmuurMateriaal'
    definition = 'Materialen van de kopmuur.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKopmuurMateriaal'
    options = {
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  definitie='beton',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKopmuurMateriaal/beton'),
        'metselwerk': KeuzelijstWaarde(invulwaarde='metselwerk',
                                       label='metselwerk',
                                       definitie='metselwerk',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKopmuurMateriaal/metselwerk')
    }

