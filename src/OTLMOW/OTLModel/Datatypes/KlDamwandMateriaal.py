# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDamwandMateriaal(KeuzelijstField):
    """Het materiaal waaruit de damwand bestaat."""
    naam = 'KlDamwandMateriaal'
    label = 'Damwand materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDamwandMateriaal'
    definition = 'Het materiaal waaruit de damwand bestaat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDamwandMateriaal'
    options = {
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='ingebruik',
                                  definitie='beton',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDamwandMateriaal/beton'),
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='hout',
                                 status='ingebruik',
                                 definitie='hout',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDamwandMateriaal/hout'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  status='ingebruik',
                                  definitie='staal',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDamwandMateriaal/staal')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

