# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTaludWaarde(KeuzelijstField):
    """De verschillende mogelijke waardes voor de hellingsgraad van de talud."""
    naam = 'KlTaludWaarde'
    label = 'Talud waarde'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTaludWaarde'
    definition = 'De verschillende mogelijke waardes voor de hellingsgraad van de talud.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTaludWaarde'
    options = {
        'tot-1-3': KeuzelijstWaarde(invulwaarde='tot-1-3',
                                    label='tot 1 3',
                                    definitie='Een hellingsgraad tot 1/3 (33,33%, 18,4°).',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludWaarde/tot-1-3'),
        'van-1-1-en-steiler': KeuzelijstWaarde(invulwaarde='van-1-1-en-steiler',
                                               label='van 1 1 en steiler',
                                               definitie='Hellingsgraad van 1/1 (100%, 45°) of steiler.',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludWaarde/van-1-1-en-steiler'),
        'van-1-2-tot-1-1': KeuzelijstWaarde(invulwaarde='van-1-2-tot-1-1',
                                            label='van 1 2 tot 1 1',
                                            definitie='Een hellingsgraad van 1/2 (50%, 26,6%) tot 1/1 (100%, 45°).',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludWaarde/van-1-2-tot-1-1'),
        'van-1-3-tot-1-2': KeuzelijstWaarde(invulwaarde='van-1-3-tot-1-2',
                                            label='van 1 3 tot 1 2',
                                            definitie='Een hellingsgraad van 1/3 (33,33%, 18,4°) tot 1/2 (50%, 26,6°).',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludWaarde/van-1-3-tot-1-2')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlTaludWaarde.get_dummy_data()

