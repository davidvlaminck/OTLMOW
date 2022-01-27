# coding=utf-8
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

