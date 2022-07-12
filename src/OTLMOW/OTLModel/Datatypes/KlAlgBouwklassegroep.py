# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgBouwklassegroep(KeuzelijstField):
    """De bouwklassegroepen."""
    naam = 'KlAlgBouwklassegroep'
    label = 'Alg bouwklassegroep'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAlgBouwklassegroep'
    definition = 'De bouwklassegroepen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgBouwklassegroep'
    options = {
        'B1': KeuzelijstWaarde(invulwaarde='B1',
                               label='B1',
                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='B1',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgBouwklassegroep/B1'),
        'B10': KeuzelijstWaarde(invulwaarde='B10',
                                label='B10',
                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='B10',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgBouwklassegroep/B10'),
        'B2': KeuzelijstWaarde(invulwaarde='B2',
                               label='B2',
                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='B2',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgBouwklassegroep/B2'),
        'B3': KeuzelijstWaarde(invulwaarde='B3',
                               label='B3',
                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='B3',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgBouwklassegroep/B3'),
        'B4': KeuzelijstWaarde(invulwaarde='B4',
                               label='B4',
                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='B4',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgBouwklassegroep/B4'),
        'B5': KeuzelijstWaarde(invulwaarde='B5',
                               label='B5',
                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='B5',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgBouwklassegroep/B5'),
        'B6': KeuzelijstWaarde(invulwaarde='B6',
                               label='B6',
                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='B6',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgBouwklassegroep/B6'),
        'B7': KeuzelijstWaarde(invulwaarde='B7',
                               label='B7',
                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='B7',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgBouwklassegroep/B7'),
        'B8': KeuzelijstWaarde(invulwaarde='B8',
                               label='B8',
                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='B8',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgBouwklassegroep/B8'),
        'B9': KeuzelijstWaarde(invulwaarde='B9',
                               label='B9',
                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='B9',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgBouwklassegroep/B9'),
        'BF': KeuzelijstWaarde(invulwaarde='BF',
                               label='BF',
                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='BF',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgBouwklassegroep/BF')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlAlgBouwklassegroep.get_dummy_data()

