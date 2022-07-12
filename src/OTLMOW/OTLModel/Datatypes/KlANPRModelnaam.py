# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlANPRModelnaam(KeuzelijstField):
    """De modelnaam van de ANPR camera."""
    naam = 'KlANPRModelnaam'
    label = 'ANPR modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlANPRModelnaam'
    definition = 'De modelnaam van de ANPR camera.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlANPRModelnaam'
    options = {
        'G1': KeuzelijstWaarde(invulwaarde='G1',
                               label='G1',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRModelnaam/G1'),
        'G3': KeuzelijstWaarde(invulwaarde='G3',
                               label='G3',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRModelnaam/G3'),
        'dual': KeuzelijstWaarde(invulwaarde='dual',
                                 label='dual',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRModelnaam/dual'),
        'i-car-cam5': KeuzelijstWaarde(invulwaarde='i-car-cam5',
                                       label='iCar cam5',
                                       status='ingebruik',
                                       definitie='iCar cam5',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRModelnaam/i-car-cam5')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlANPRModelnaam.get_dummy_data()

