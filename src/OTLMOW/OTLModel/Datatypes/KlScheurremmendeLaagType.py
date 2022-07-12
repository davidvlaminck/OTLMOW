# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlScheurremmendeLaagType(KeuzelijstField):
    """Types van scheurremmende laag."""
    naam = 'KlScheurremmendeLaagType'
    label = 'Scheurremmende laag type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlScheurremmendeLaagType'
    definition = 'Types van scheurremmende laag.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlScheurremmendeLaagType'
    options = {
        'bitumineus-membraan-(SAMI)': KeuzelijstWaarde(invulwaarde='bitumineus-membraan-(SAMI)',
                                                       label='bitumineus membraan (SAMI)',
                                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                       definitie='bitumineus membraan (SAMI)',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/bitumineus-membraan-(SAMI)'),
        'geocomposiet': KeuzelijstWaarde(invulwaarde='geocomposiet',
                                         label='geocomposiet',
                                         status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie='geocomposiet',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/geocomposiet'),
        'geocomposiet-klasse-c': KeuzelijstWaarde(invulwaarde='geocomposiet-klasse-c',
                                                  label='geocomposiet klasse C',
                                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                  definitie='geocomposiet klasse C',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/geocomposiet-klasse-c'),
        'geocomposiet-klasse-cd': KeuzelijstWaarde(invulwaarde='geocomposiet-klasse-cd',
                                                   label='geocomposiet klasse CD',
                                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                   definitie='geocomposiet klasse CD',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/geocomposiet-klasse-cd'),
        'geocomposiet-klasse-d': KeuzelijstWaarde(invulwaarde='geocomposiet-klasse-d',
                                                  label='geocomposiet klasse D',
                                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                  definitie='geocomposiet klasse D',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/geocomposiet-klasse-d'),
        'geocomposiet-klasse-e-1': KeuzelijstWaarde(invulwaarde='geocomposiet-klasse-e-1',
                                                    label='geocomposiet klasse E1',
                                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                    definitie='geocomposiet klasse E1',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/geocomposiet-klasse-e-1'),
        'geocomposiet-klasse-e-2': KeuzelijstWaarde(invulwaarde='geocomposiet-klasse-e-2',
                                                    label='geocomposiet klasse E2',
                                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                    definitie='geocomposiet klasse E2',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/geocomposiet-klasse-e-2'),
        'grids': KeuzelijstWaarde(invulwaarde='grids',
                                  label='grids',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='grids',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/grids'),
        'grids-klasse-c': KeuzelijstWaarde(invulwaarde='grids-klasse-c',
                                           label='grids klasse C',
                                           status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='grids klasse C',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/grids-klasse-c'),
        'grids-klasse-cd': KeuzelijstWaarde(invulwaarde='grids-klasse-cd',
                                            label='grids klasse CD',
                                            status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            definitie='grids klasse CD',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/grids-klasse-cd'),
        'grids-klasse-d': KeuzelijstWaarde(invulwaarde='grids-klasse-d',
                                           label='grids klasse D',
                                           status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='grids klasse D',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/grids-klasse-d'),
        'grids-klasse-e-1': KeuzelijstWaarde(invulwaarde='grids-klasse-e-1',
                                             label='grids klasse E1',
                                             status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                             definitie='grids klasse E1',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/grids-klasse-e-1'),
        'grids-klasse-e-2': KeuzelijstWaarde(invulwaarde='grids-klasse-e-2',
                                             label='grids klasse E2',
                                             status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                             definitie='grids klasse E2',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/grids-klasse-e-2'),
        'stalen-wapeningsnet-type-1': KeuzelijstWaarde(invulwaarde='stalen-wapeningsnet-type-1',
                                                       label='stalen wapeningsnet type 1',
                                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                       definitie='stalen wapeningsnet type 1',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/stalen-wapeningsnet-type-1'),
        'stalen-wapeningsnet-type-2': KeuzelijstWaarde(invulwaarde='stalen-wapeningsnet-type-2',
                                                       label='stalen wapeningsnet type 2',
                                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                       definitie='stalen wapeningsnet type 2',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlScheurremmendeLaagType/stalen-wapeningsnet-type-2')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlScheurremmendeLaagType.get_dummy_data()

