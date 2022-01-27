# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBinnenverlichtingstoestelSchakelwijze(KeuzelijstField):
    """Lijst met schakelwijzen voor een binnenverlichtingstoestel."""
    naam = 'KlBinnenverlichtingstoestelSchakelwijze'
    label = 'Binnenverlichtingstoestel schakelwijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBinnenverlichtingstoestelSchakelwijze'
    definition = 'Lijst met schakelwijzen voor een binnenverlichtingstoestel.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBinnenverlichtingstoestelSchakelwijze'
    options = {
        'continu': KeuzelijstWaarde(invulwaarde='continu',
                                    label='continu',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSchakelwijze/continu'),
        'schakelaar': KeuzelijstWaarde(invulwaarde='schakelaar',
                                       label='schakelaar',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSchakelwijze/schakelaar'),
        'timer': KeuzelijstWaarde(invulwaarde='timer',
                                  label='timer',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSchakelwijze/timer')
    }

