# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBinnenverlichtingstoestelSchakelwijze(KeuzelijstField):
    """Lijst met schakelwijzen voor een binnenverlichtingstoestel."""
    naam = 'KlBinnenverlichtingstoestelSchakelwijze'
    label = 'Binnenverlichtingstoestel schakelwijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBinnenverlichtingstoestelSchakelwijze'
    definition = 'Lijst met schakelwijzen voor een binnenverlichtingstoestel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBinnenverlichtingstoestelSchakelwijze'
    options = {
        'continu': KeuzelijstWaarde(invulwaarde='continu',
                                    label='continu',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSchakelwijze/continu'),
        'schakelaar': KeuzelijstWaarde(invulwaarde='schakelaar',
                                       label='schakelaar',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSchakelwijze/schakelaar'),
        'timer': KeuzelijstWaarde(invulwaarde='timer',
                                  label='timer',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSchakelwijze/timer')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBinnenverlichtingstoestelSchakelwijze.get_dummy_data()

