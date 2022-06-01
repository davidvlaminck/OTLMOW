# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEKantopsluitingKleur(KeuzelijstField):
    """De kleur van de kantopsluiting."""
    naam = 'KlLEKantopsluitingKleur'
    label = 'Kantopsluiting kleur'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEKantopsluitingKleur'
    definition = 'De kleur van de kantopsluiting.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEKantopsluitingKleur'
    options = {
        'gekleurd': KeuzelijstWaarde(invulwaarde='gekleurd',
                                     label='gekleurd',
                                     definitie='gekleurd',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/gekleurd'),
        'grijs': KeuzelijstWaarde(invulwaarde='grijs',
                                  label='grijs',
                                  definitie='grijs',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/grijs'),
        'oker': KeuzelijstWaarde(invulwaarde='oker',
                                 label='oker',
                                 definitie='oker',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/oker'),
        'rood': KeuzelijstWaarde(invulwaarde='rood',
                                 label='rood',
                                 definitie='rood',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/rood'),
        'wit': KeuzelijstWaarde(invulwaarde='wit',
                                label='wit',
                                definitie='wit',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/wit'),
        'zwart': KeuzelijstWaarde(invulwaarde='zwart',
                                  label='zwart',
                                  definitie='zwart',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/zwart')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlLEKantopsluitingKleur.get_dummy_data()

