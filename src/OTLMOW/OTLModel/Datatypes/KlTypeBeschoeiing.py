# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeBeschoeiing(KeuzelijstField):
    """Type beschoeiing."""
    naam = 'KlTypeBeschoeiing'
    label = 'Type beschoeiing'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeBeschoeiing'
    definition = 'Type beschoeiing.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBeschoeiing'
    options = {
        'Berliner': KeuzelijstWaarde(invulwaarde='Berliner',
                                     label='Berliner',
                                     definitie='Berliner',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeschoeiing/Berliner'),
        'Krings': KeuzelijstWaarde(invulwaarde='Krings',
                                   label='Krings',
                                   definitie='Krings',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeschoeiing/Krings')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlTypeBeschoeiing.get_dummy_data()

