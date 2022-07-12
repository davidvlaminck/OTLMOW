# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPlaatsingswijze(KeuzelijstField):
    """Mogelijke manieren van plaatsing van het straatmeubilair."""
    naam = 'KlPlaatsingswijze'
    label = 'Plaatsingswijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPlaatsingswijze'
    definition = 'Mogelijke manieren van plaatsing van het straatmeubilair.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPlaatsingswijze'
    options = {
        'vast': KeuzelijstWaarde(invulwaarde='vast',
                                 label='vast',
                                 status='ingebruik',
                                 definitie='Vaste plaatsing van het straatmeubilair.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlaatsingswijze/vast'),
        'wegneembaar': KeuzelijstWaarde(invulwaarde='wegneembaar',
                                        label='wegneembaar',
                                        status='ingebruik',
                                        definitie='Wegneembare plaatsing van het straatmeubilair.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlaatsingswijze/wegneembaar')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlPlaatsingswijze.get_dummy_data()

