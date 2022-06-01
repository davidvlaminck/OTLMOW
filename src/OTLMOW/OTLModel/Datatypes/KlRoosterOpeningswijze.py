# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRoosterOpeningswijze(KeuzelijstField):
    """Deze keuzelijst geeft de manier aan hoe het rooster geopend kan worden."""
    naam = 'KlRoosterOpeningswijze'
    label = 'Rooster openingswijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRoosterOpeningswijze'
    definition = 'Deze keuzelijst geeft de manier aan hoe het rooster geopend kan worden.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRoosterOpeningswijze'
    options = {
        'ovaal-deksel': KeuzelijstWaarde(invulwaarde='ovaal-deksel',
                                         label='ovaal deksel',
                                         definitie='ovaal deksel',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRoosterOpeningswijze/ovaal-deksel'),
        'scharnierend': KeuzelijstWaarde(invulwaarde='scharnierend',
                                         label='scharnierend',
                                         definitie='scharnierend',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRoosterOpeningswijze/scharnierend'),
        'uitneembaar': KeuzelijstWaarde(invulwaarde='uitneembaar',
                                        label='uitneembaar',
                                        definitie='uitneembaar',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRoosterOpeningswijze/uitneembaar')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlRoosterOpeningswijze.get_dummy_data()

