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
        'R1': KeuzelijstWaarde(invulwaarde='R1',
                               label='R1',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R1'),
        'R2': KeuzelijstWaarde(invulwaarde='R2',
                               label='R2',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R2'),
        'R3': KeuzelijstWaarde(invulwaarde='R3',
                               label='R3',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R3'),
        'R4': KeuzelijstWaarde(invulwaarde='R4',
                               label='R4',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R4'),
        'R5': KeuzelijstWaarde(invulwaarde='R5',
                               label='R5',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R5'),
        'R6': KeuzelijstWaarde(invulwaarde='R6',
                               label='R6',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R6')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlWvLedAantalTeVerlichtenRijstroken.get_dummy_data()

