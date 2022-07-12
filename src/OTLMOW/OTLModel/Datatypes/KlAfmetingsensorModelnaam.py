# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfmetingsensorModelnaam(KeuzelijstField):
    """De modelnaam van de afmetingsensor."""
    naam = 'KlAfmetingsensorModelnaam'
    label = 'Afmetingsensor modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfmetingsensorModelnaam'
    definition = 'De modelnaam van de afmetingsensor.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfmetingsensorModelnaam'
    options = {
        'FPS': KeuzelijstWaarde(invulwaarde='FPS',
                                label='FPS',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfmetingsensorModelnaam/FPS'),
        'LMS': KeuzelijstWaarde(invulwaarde='LMS',
                                label='LMS',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfmetingsensorModelnaam/LMS')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlAfmetingsensorModelnaam.get_dummy_data()

