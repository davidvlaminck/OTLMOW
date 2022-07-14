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
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEKantopsluitingKleur'
    options = {
        'gekleurd': KeuzelijstWaarde(invulwaarde='gekleurd',
                                     label='gekleurd',
                                     status='ingebruik',
                                     definitie='gekleurd',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/gekleurd'),
        'grijs': KeuzelijstWaarde(invulwaarde='grijs',
                                  label='grijs',
                                  status='ingebruik',
                                  definitie='grijs',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/grijs'),
        'oker': KeuzelijstWaarde(invulwaarde='oker',
                                 label='oker',
                                 status='ingebruik',
                                 definitie='oker',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/oker'),
        'rood': KeuzelijstWaarde(invulwaarde='rood',
                                 label='rood',
                                 status='ingebruik',
                                 definitie='rood',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/rood'),
        'wit': KeuzelijstWaarde(invulwaarde='wit',
                                label='wit',
                                status='ingebruik',
                                definitie='wit',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/wit'),
        'zwart': KeuzelijstWaarde(invulwaarde='zwart',
                                  label='zwart',
                                  status='ingebruik',
                                  definitie='zwart',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/zwart')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

