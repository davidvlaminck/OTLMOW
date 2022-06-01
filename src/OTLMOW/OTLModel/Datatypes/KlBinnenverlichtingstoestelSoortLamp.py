# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBinnenverlichtingstoestelSoortLamp(KeuzelijstField):
    """Lijst van mogelijke soorten lampen voor binnenverlichtingstoestellen."""
    naam = 'KlBinnenverlichtingstoestelSoortLamp'
    label = 'Binnenverlichtingstoestel soort lamp'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBinnenverlichtingstoestelSoortLamp'
    definition = 'Lijst van mogelijke soorten lampen voor binnenverlichtingstoestellen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBinnenverlichtingstoestelSoortLamp'
    options = {
        'LED': KeuzelijstWaarde(invulwaarde='LED',
                                label='LED',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSoortLamp/LED'),
        'TL': KeuzelijstWaarde(invulwaarde='TL',
                               label='TL',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSoortLamp/TL'),
        'gloeilamp': KeuzelijstWaarde(invulwaarde='gloeilamp',
                                      label='gloeilamp',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSoortLamp/gloeilamp'),
        'halogeen': KeuzelijstWaarde(invulwaarde='halogeen',
                                     label='halogeen',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSoortLamp/halogeen'),
        'spaarlamp': KeuzelijstWaarde(invulwaarde='spaarlamp',
                                      label='spaarlamp',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSoortLamp/spaarlamp')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBinnenverlichtingstoestelSoortLamp.get_dummy_data()

