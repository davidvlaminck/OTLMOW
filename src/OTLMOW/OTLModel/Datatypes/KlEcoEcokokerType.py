# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEcoEcokokerType(KeuzelijstField):
    """Types van ecokoker."""
    naam = 'KlEcoEcokokerType'
    label = 'Ecokoker type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEcoEcokokerType'
    definition = 'Types van ecokoker.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEcoEcokokerType'
    options = {
        'amfibieenkoker': KeuzelijstWaarde(invulwaarde='amfibieenkoker',
                                           label='amfibieenkoker',
                                           status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='Een ecokoker voor amfibieën.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoEcokokerType/amfibieenkoker'),
        'betonnen-ecokoker': KeuzelijstWaarde(invulwaarde='betonnen-ecokoker',
                                              label='betonnen ecokoker',
                                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                              definitie='Een ecokoker uit beton.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoEcokokerType/betonnen-ecokoker')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlEcoEcokokerType.get_dummy_data()

