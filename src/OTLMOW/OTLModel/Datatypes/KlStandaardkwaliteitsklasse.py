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
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStandaardkwaliteitsklasse'
    options = {
        'a': KeuzelijstWaarde(invulwaarde='a',
                              label='a',
                              definitie='A',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStandaardkwaliteitsklasse/a'),
        'b': KeuzelijstWaarde(invulwaarde='b',
                              label='b',
                              definitie='B',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStandaardkwaliteitsklasse/b'),
        'c': KeuzelijstWaarde(invulwaarde='c',
                              label='c',
                              definitie='C',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStandaardkwaliteitsklasse/c'),
        'd': KeuzelijstWaarde(invulwaarde='d',
                              label='d',
                              definitie='D',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStandaardkwaliteitsklasse/d'),
        'e': KeuzelijstWaarde(invulwaarde='e',
                              label='e',
                              definitie='E',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStandaardkwaliteitsklasse/e')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlStandaardkwaliteitsklasse.get_dummy_data()

