# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRoosterIndeling(KeuzelijstField):
    """Deze keuzelijst geeft aan hoe het rooster ingedeeld is: met zijdelingse opvang of dat er sprake is van een 1-delig of 2-delig rooster."""
    naam = 'KlRoosterIndeling'
    label = 'Rooster indeling'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRoosterIndeling'
    definition = 'Deze keuzelijst geeft aan hoe het rooster ingedeeld is: met zijdelingse opvang of dat er sprake is van een 1-delig of 2-delig rooster.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRoosterIndeling'
    options = {
        '1-delig': KeuzelijstWaarde(invulwaarde='1-delig',
                                    label='1-delig',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='1-delig',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRoosterIndeling/1-delig'),
        '2-delig': KeuzelijstWaarde(invulwaarde='2-delig',
                                    label='2-delig',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='2-delig',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRoosterIndeling/2-delig'),
        'zijdelingse-opvang': KeuzelijstWaarde(invulwaarde='zijdelingse-opvang',
                                               label='zijdelingse opvang',
                                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                               definitie='zijdelingse opvang',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRoosterIndeling/zijdelingse-opvang')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlRoosterIndeling.get_dummy_data()

