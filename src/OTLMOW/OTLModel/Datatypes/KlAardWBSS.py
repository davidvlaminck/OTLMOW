# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAardWBSS(KeuzelijstField):
    """De mogelijke vormen die ervoor zorgen dat hemelwater infiltreert langs de waterdoorlatende betonstraatsteen."""
    naam = 'KlAardWBSS'
    label = 'Aard van waterdoorlatende betonstraatsteen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAardWBSS'
    definition = 'De mogelijke vormen die ervoor zorgen dat hemelwater infiltreert langs de waterdoorlatende betonstraatsteen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAardWBSS'
    options = {
        'met-drainageopeningen': KeuzelijstWaarde(invulwaarde='met-drainageopeningen',
                                                  label='met drainageopeningen',
                                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                  definitie='Vorm voor waterdoorlatende betonstraatsteen waarbij hemelwater infiltreert langs de betonstraatsteen.',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardWBSS/met-drainageopeningen'),
        'met-verbrede-voegen': KeuzelijstWaarde(invulwaarde='met-verbrede-voegen',
                                                label='met verbrede voegen',
                                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                definitie='Vorm voor waterdoorlatende betonstraatsteen waarbij hemelwater infiltreert langs de betonstraatsteen.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardWBSS/met-verbrede-voegen'),
        'poreus-beton': KeuzelijstWaarde(invulwaarde='poreus-beton',
                                         label='poreus beton',
                                         status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie='Vorm voor waterdoorlatende betonstraatsteen waarbij hemelwater infiltreert doorheen de betonstraatsteen.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardWBSS/poreus-beton')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlAardWBSS.get_dummy_data()

