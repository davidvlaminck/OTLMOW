# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKopmuurMateriaal(KeuzelijstField):
    """Materialen van de kopmuur."""
    naam = 'KlKopmuurMateriaal'
    label = 'Kopmuur materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKopmuurMateriaal'
    definition = 'Materialen van de kopmuur.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKopmuurMateriaal'
    options = {
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='ingebruik',
                                  definitie='beton',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKopmuurMateriaal/beton'),
        'metselwerk': KeuzelijstWaarde(invulwaarde='metselwerk',
                                       label='metselwerk',
                                       status='ingebruik',
                                       definitie='metselwerk',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKopmuurMateriaal/metselwerk')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

