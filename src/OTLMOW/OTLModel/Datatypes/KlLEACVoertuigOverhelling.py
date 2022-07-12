# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACVoertuigOverhelling(KeuzelijstField):
    """De verschillende maten van voertuigoverhelling."""
    naam = 'KlLEACVoertuigOverhelling'
    label = 'Voertuig overhelling'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACVoertuigOverhelling'
    definition = 'De verschillende maten van voertuigoverhelling.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACVoertuigOverhelling'
    options = {
        'vIn1': KeuzelijstWaarde(invulwaarde='vIn1',
                                 label='vIn1',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='VIn <= 0.6',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACVoertuigOverhelling/vIn1'),
        'vIn2': KeuzelijstWaarde(invulwaarde='vIn2',
                                 label='vIn2',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='VIn <= 0.8',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACVoertuigOverhelling/vIn2'),
        'vIn3': KeuzelijstWaarde(invulwaarde='vIn3',
                                 label='vIn3',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='VIn <= 1.0',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACVoertuigOverhelling/vIn3'),
        'vIn4': KeuzelijstWaarde(invulwaarde='vIn4',
                                 label='vIn4',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='VIn <= 1.3',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACVoertuigOverhelling/vIn4'),
        'vIn5': KeuzelijstWaarde(invulwaarde='vIn5',
                                 label='vIn5',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='VIn <= 1.7',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACVoertuigOverhelling/vIn5'),
        'vIn6': KeuzelijstWaarde(invulwaarde='vIn6',
                                 label='vIn6',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='VIn <= 2.1',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACVoertuigOverhelling/vIn6'),
        'vIn7': KeuzelijstWaarde(invulwaarde='vIn7',
                                 label='vIn7',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='VIn <= 2.5',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACVoertuigOverhelling/vIn7'),
        'vIn8': KeuzelijstWaarde(invulwaarde='vIn8',
                                 label='vIn8',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='VIn <= 3.5',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACVoertuigOverhelling/vIn8'),
        'vIn9': KeuzelijstWaarde(invulwaarde='vIn9',
                                 label='vIn9',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='VIn > 3.5',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACVoertuigOverhelling/vIn9')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlLEACVoertuigOverhelling.get_dummy_data()

