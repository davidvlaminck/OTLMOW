# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCabineAardingsstelsel(KeuzelijstField):
    """Lijst van mogelijke aardinggsstelsels."""
    naam = 'KlCabineAardingsstelsel'
    label = 'Cabine aardingsstelsel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCabineAardingsstelsel'
    definition = 'Lijst van mogelijke aardinggsstelsels.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCabineAardingsstelsel'
    options = {
        'gescheiden': KeuzelijstWaarde(invulwaarde='gescheiden',
                                       label='gescheiden',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineAardingsstelsel/gescheiden'),
        'globaal': KeuzelijstWaarde(invulwaarde='globaal',
                                    label='globaal',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineAardingsstelsel/globaal')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlCabineAardingsstelsel.get_dummy_data()

