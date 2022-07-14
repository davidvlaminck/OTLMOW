# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLedLichtpunthoogte(KeuzelijstField):
    """Hoogte van het lichtpunt ten opzichte van de rijweg."""
    naam = 'KlWvLedLichtpunthoogte'
    label = 'WV LED lichtpunthoogte'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedLichtpunthoogte'
    definition = 'Hoogte van het lichtpunt ten opzichte van de rijweg.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedLichtpunthoogte'
    options = {
        '10': KeuzelijstWaarde(invulwaarde='10',
                               label='10',
                               status='ingebruik',
                               definitie='10',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/10'),
        '12-5': KeuzelijstWaarde(invulwaarde='12-5',
                                 label='12.5',
                                 status='ingebruik',
                                 definitie='12,5',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/12-5'),
        '16': KeuzelijstWaarde(invulwaarde='16',
                               label='16',
                               status='ingebruik',
                               definitie='16',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/16'),
        '20': KeuzelijstWaarde(invulwaarde='20',
                               label='20',
                               status='ingebruik',
                               definitie='20',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/20'),
        '3-2': KeuzelijstWaarde(invulwaarde='3-2',
                                label='3.2',
                                status='ingebruik',
                                definitie='3,2',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/3-2'),
        '4': KeuzelijstWaarde(invulwaarde='4',
                              label='4',
                              status='ingebruik',
                              definitie='4',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/4'),
        '5': KeuzelijstWaarde(invulwaarde='5',
                              label='5',
                              status='ingebruik',
                              definitie='5',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/5'),
        '6-3': KeuzelijstWaarde(invulwaarde='6-3',
                                label='6.3',
                                status='ingebruik',
                                definitie='6,3',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/6-3'),
        '7': KeuzelijstWaarde(invulwaarde='7',
                              label='7',
                              status='ingebruik',
                              definitie='7',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/7'),
        '8': KeuzelijstWaarde(invulwaarde='8',
                              label='8',
                              status='ingebruik',
                              definitie='8',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/8'),
        'H04': KeuzelijstWaarde(invulwaarde='H04',
                                label='H04',
                                status='uitgebruik',
                                definitie='H04',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H04'),
        'H05': KeuzelijstWaarde(invulwaarde='H05',
                                label='H05',
                                status='uitgebruik',
                                definitie='H05',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H05'),
        'H06': KeuzelijstWaarde(invulwaarde='H06',
                                label='H06',
                                status='uitgebruik',
                                definitie='H06',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H06'),
        'H08': KeuzelijstWaarde(invulwaarde='H08',
                                label='H08',
                                status='uitgebruik',
                                definitie='H08',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H08'),
        'H10': KeuzelijstWaarde(invulwaarde='H10',
                                label='H10',
                                status='uitgebruik',
                                definitie='H10',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H10'),
        'H12': KeuzelijstWaarde(invulwaarde='H12',
                                label='H12',
                                status='uitgebruik',
                                definitie='H12',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H12'),
        'H16': KeuzelijstWaarde(invulwaarde='H16',
                                label='H16',
                                status='uitgebruik',
                                definitie='H16',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H16'),
        'H18': KeuzelijstWaarde(invulwaarde='H18',
                                label='H18',
                                status='uitgebruik',
                                definitie='H18',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H18'),
        'H20': KeuzelijstWaarde(invulwaarde='H20',
                                label='H20',
                                status='uitgebruik',
                                definitie='H20',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H20')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlWvLedLichtpunthoogte.get_dummy_data()

