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
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRoosterOpeningswijze'
    options = {
        'ovaal-deksel': KeuzelijstWaarde(invulwaarde='ovaal-deksel',
                                         label='ovaal deksel',
                                         status='ingebruik',
                                         definitie='ovaal deksel',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRoosterOpeningswijze/ovaal-deksel'),
        'scharnierend': KeuzelijstWaarde(invulwaarde='scharnierend',
                                         label='scharnierend',
                                         status='ingebruik',
                                         definitie='scharnierend',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRoosterOpeningswijze/scharnierend'),
        'uitneembaar': KeuzelijstWaarde(invulwaarde='uitneembaar',
                                        label='uitneembaar',
                                        status='ingebruik',
                                        definitie='uitneembaar',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRoosterOpeningswijze/uitneembaar')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

