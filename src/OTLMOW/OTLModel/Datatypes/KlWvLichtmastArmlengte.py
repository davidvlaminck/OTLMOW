# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLichtmastArmlengte(KeuzelijstField):
    """Lengte van de arm van de lichtmast in meter."""
    naam = 'KlWvLichtmastArmlengte'
    label = 'WV-mast armlengte'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLichtmastArmlengte'
    definition = 'Lengte van de arm van de lichtmast in meter.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLichtmastArmlengte'
    options = {
        '1.5': KeuzelijstWaarde(invulwaarde='1.5',
                                label='1.5',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastArmlengte/1.5'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='2',
                              status='ingebruik',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastArmlengte/2'),
        '2.5': KeuzelijstWaarde(invulwaarde='2.5',
                                label='2.5',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastArmlengte/2.5'),
        '3.2': KeuzelijstWaarde(invulwaarde='3.2',
                                label='3.2',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastArmlengte/3.2'),
        'niet-van-toepassing': KeuzelijstWaarde(invulwaarde='niet-van-toepassing',
                                                label='niet van toepassing',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastArmlengte/niet-van-toepassing')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlWvLichtmastArmlengte.get_dummy_data()

