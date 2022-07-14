# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStandaardkwaliteitsklasse(KeuzelijstField):
    """De mogelijke tandaardkwaliteitsklassen."""
    naam = 'KlStandaardkwaliteitsklasse'
    label = 'Standaardkwaliteitsklasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStandaardkwaliteitsklasse'
    definition = 'De mogelijke tandaardkwaliteitsklassen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStandaardkwaliteitsklasse'
    options = {
        'a': KeuzelijstWaarde(invulwaarde='a',
                              label='a',
                              status='ingebruik',
                              definitie='A',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStandaardkwaliteitsklasse/a'),
        'b': KeuzelijstWaarde(invulwaarde='b',
                              label='b',
                              status='ingebruik',
                              definitie='B',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStandaardkwaliteitsklasse/b'),
        'c': KeuzelijstWaarde(invulwaarde='c',
                              label='c',
                              status='ingebruik',
                              definitie='C',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStandaardkwaliteitsklasse/c'),
        'd': KeuzelijstWaarde(invulwaarde='d',
                              label='d',
                              status='ingebruik',
                              definitie='D',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStandaardkwaliteitsklasse/d'),
        'e': KeuzelijstWaarde(invulwaarde='e',
                              label='e',
                              status='ingebruik',
                              definitie='E',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStandaardkwaliteitsklasse/e')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

