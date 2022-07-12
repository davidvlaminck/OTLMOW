# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVegetatiePlantverband(KeuzelijstField):
    """De verschillende opties voor het plantverband."""
    naam = 'KlVegetatiePlantverband'
    label = 'Vegetatie plantverband'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVegetatiePlantverband'
    definition = 'De verschillende opties voor het plantverband.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVegetatiePlantverband'
    options = {
        'geschrankt': KeuzelijstWaarde(invulwaarde='geschrankt',
                                       label='geschrankt',
                                       status='ingebruik',
                                       definitie='De planten staan geschrankt',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatiePlantverband/geschrankt'),
        'rijafstand': KeuzelijstWaarde(invulwaarde='rijafstand',
                                       label='rijafstand',
                                       status='ingebruik',
                                       definitie='De afstand tussen de rijen',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatiePlantverband/rijafstand')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlVegetatiePlantverband.get_dummy_data()

