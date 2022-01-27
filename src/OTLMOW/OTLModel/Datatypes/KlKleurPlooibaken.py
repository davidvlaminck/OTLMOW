# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKleurPlooibaken(KeuzelijstField):
    """Kleuropties voor het plooibaken."""
    naam = 'KlKleurPlooibaken'
    label = 'Kleur plooibaken'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKleurPlooibaken'
    definition = 'Kleuropties voor het plooibaken.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKleurPlooibaken'
    options = {
        'blauw': KeuzelijstWaarde(invulwaarde='blauw',
                                  label='blauw',
                                  definitie='blauw',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurPlooibaken/blauw'),
        'geel': KeuzelijstWaarde(invulwaarde='geel',
                                 label='geel',
                                 definitie='geel',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurPlooibaken/geel'),
        'grijs': KeuzelijstWaarde(invulwaarde='grijs',
                                  label='grijs',
                                  definitie='grijs',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurPlooibaken/grijs'),
        'groen': KeuzelijstWaarde(invulwaarde='groen',
                                  label='groen',
                                  definitie='groen',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurPlooibaken/groen'),
        'oranje': KeuzelijstWaarde(invulwaarde='oranje',
                                   label='oranje',
                                   definitie='oranje',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurPlooibaken/oranje'),
        'rood': KeuzelijstWaarde(invulwaarde='rood',
                                 label='rood',
                                 definitie='rood',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurPlooibaken/rood'),
        'zwart': KeuzelijstWaarde(invulwaarde='zwart',
                                  label='zwart',
                                  definitie='zwart',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurPlooibaken/zwart')
    }

