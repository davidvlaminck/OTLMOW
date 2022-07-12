# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoogpaalType(KeuzelijstField):
    """Draagwijdte van de boogpaal."""
    naam = 'KlBoogpaalType'
    label = 'Type boogpaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoogpaalType'
    definition = 'Draagwijdte van de boogpaal.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoogpaalType'
    options = {
        '3.50': KeuzelijstWaarde(invulwaarde='3.50',
                                 label='3.50',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='middelgrote draagwijdte',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoogpaalType/3.50'),
        '7.50': KeuzelijstWaarde(invulwaarde='7.50',
                                 label='7.50',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='grote draagwijdte',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoogpaalType/7.50')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBoogpaalType.get_dummy_data()

