# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLedAantalTeVerlichtenRijstroken(KeuzelijstField):
    """Het aantal rijstroken dat verlicht wordt door het LED verlichtingstoestel."""
    naam = 'KlWvLedAantalTeVerlichtenRijstroken'
    label = 'WV LED aantal te verlichten rijstroken'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedAantalTeVerlichtenRijstroken'
    definition = 'Het aantal rijstroken dat verlicht wordt door het LED verlichtingstoestel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedAantalTeVerlichtenRijstroken'
    options = {
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='1',
                              status='ingebruik',
                              definitie='1 rijstrook',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/1'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='2',
                              status='ingebruik',
                              definitie='2 rijstroken',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/2'),
        '3': KeuzelijstWaarde(invulwaarde='3',
                              label='3',
                              status='ingebruik',
                              definitie='3 rijstroken',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/3'),
        '4': KeuzelijstWaarde(invulwaarde='4',
                              label='4',
                              status='ingebruik',
                              definitie='4 rijstroken',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/4'),
        '5': KeuzelijstWaarde(invulwaarde='5',
                              label='5',
                              status='ingebruik',
                              definitie='5 rijstroken',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/5'),
        '6': KeuzelijstWaarde(invulwaarde='6',
                              label='6',
                              status='ingebruik',
                              definitie='6 rijstroken',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/6'),
        'R1': KeuzelijstWaarde(invulwaarde='R1',
                               label='R1',
                               status='uitgebruik',
                               definitie='R1',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R1'),
        'R2': KeuzelijstWaarde(invulwaarde='R2',
                               label='R2',
                               status='uitgebruik',
                               definitie='R2',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R2'),
        'R3': KeuzelijstWaarde(invulwaarde='R3',
                               label='R3',
                               status='uitgebruik',
                               definitie='R3',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R3'),
        'R4': KeuzelijstWaarde(invulwaarde='R4',
                               label='R4',
                               status='uitgebruik',
                               definitie='R4',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R4'),
        'R5': KeuzelijstWaarde(invulwaarde='R5',
                               label='R5',
                               status='uitgebruik',
                               definitie='R5',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R5'),
        'R6': KeuzelijstWaarde(invulwaarde='R6',
                               label='R6',
                               status='uitgebruik',
                               definitie='R6',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R6')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlWvLedAantalTeVerlichtenRijstroken.get_dummy_data()

