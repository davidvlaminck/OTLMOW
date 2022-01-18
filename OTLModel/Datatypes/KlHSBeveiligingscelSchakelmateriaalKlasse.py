# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHSBeveiligingscelSchakelmateriaalKlasse(KeuzelijstField):
    """Klasse van het schakelmateriaal volgens Synergrid."""
    naam = 'KlHSBeveiligingscelSchakelmateriaalKlasse'
    label = 'HS-beveiligingscel schakelmateriaal klasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHSBeveiligingscelSchakelmateriaalKlasse'
    definition = 'Klasse van het schakelmateriaal volgens Synergrid.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHSBeveiligingscelSchakelmateriaalKlasse'
    options = {
        'AA10': KeuzelijstWaarde(invulwaarde='AA10',
                                 label='AA10',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelSchakelmateriaalKlasse/AA10'),
        'AA15': KeuzelijstWaarde(invulwaarde='AA15',
                                 label='AA15',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelSchakelmateriaalKlasse/AA15'),
        'AA20': KeuzelijstWaarde(invulwaarde='AA20',
                                 label='AA20',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelSchakelmateriaalKlasse/AA20'),
        'AA31': KeuzelijstWaarde(invulwaarde='AA31',
                                 label='AA31',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelSchakelmateriaalKlasse/AA31'),
        'AA32': KeuzelijstWaarde(invulwaarde='AA32',
                                 label='AA32',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelSchakelmateriaalKlasse/AA32'),
        'AA33': KeuzelijstWaarde(invulwaarde='AA33',
                                 label='AA33',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelSchakelmateriaalKlasse/AA33'),
        'AA35': KeuzelijstWaarde(invulwaarde='AA35',
                                 label='AA35',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelSchakelmateriaalKlasse/AA35'),
        'AA40': KeuzelijstWaarde(invulwaarde='AA40',
                                 label='AA40',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelSchakelmateriaalKlasse/AA40')
    }

