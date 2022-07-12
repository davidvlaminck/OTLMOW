# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBuitenkastVerfraaid(KeuzelijstField):
    """Mogelijke types voor verfraaiing als combinatie van aan- en afwezigheid en al dan niet vegund."""
    naam = 'KlBuitenkastVerfraaid'
    label = 'Verfraaiing buitenkast'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlBuitenkastVerfraaid'
    definition = 'Mogelijke types voor verfraaiing als combinatie van aan- en afwezigheid en al dan niet vegund.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBuitenkastVerfraaid'
    options = {
        'ja': KeuzelijstWaarde(invulwaarde='ja',
                               label='ja',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBuitenkastVerfraaid/ja'),
        'ja-niet-vergund': KeuzelijstWaarde(invulwaarde='ja-niet-vergund',
                                            label='ja niet vergund',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBuitenkastVerfraaid/ja-niet-vergund'),
        'nee': KeuzelijstWaarde(invulwaarde='nee',
                                label='nee',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBuitenkastVerfraaid/nee')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBuitenkastVerfraaid.get_dummy_data()

