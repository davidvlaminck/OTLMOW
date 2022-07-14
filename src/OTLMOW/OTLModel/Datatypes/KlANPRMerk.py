# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlANPRMerk(KeuzelijstField):
    """Het merk van de ANPR-camera."""
    naam = 'KlANPRMerk'
    label = 'ANPR-camera merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlANPRMerk'
    definition = 'Het merk van de ANPR-camera.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlANPRMerk'
    options = {
        'Macq': KeuzelijstWaarde(invulwaarde='Macq',
                                 label='Macq',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRMerk/Macq'),
        'Tattile': KeuzelijstWaarde(invulwaarde='Tattile',
                                    label='Tattile',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRMerk/Tattile')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

