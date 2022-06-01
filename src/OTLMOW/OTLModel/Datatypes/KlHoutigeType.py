# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHoutigeType(KeuzelijstField):
    """Types van houtige vegetatie."""
    naam = 'KlHoutigeType'
    label = 'Type houtige vegetatie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHoutigeType'
    definition = 'Types van houtige vegetatie.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHoutigeType'
    options = {
        'bomen---bos': KeuzelijstWaarde(invulwaarde='bomen---bos',
                                        label='bomen - bos',
                                        definitie='Opgaande beplanting van houtachtige gewassen die boomvormend zijn.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHoutigeType/bomen---bos'),
        'houtkant': KeuzelijstWaarde(invulwaarde='houtkant',
                                     label='houtkant',
                                     definitie='Een houtkant is een lijnvormige begroeiing met houtgewas (combinatie van bomen en struiken) met een minimale breedte van 3meter en meer en minstens 1 plantrij. ',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHoutigeType/houtkant')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlHoutigeType.get_dummy_data()

