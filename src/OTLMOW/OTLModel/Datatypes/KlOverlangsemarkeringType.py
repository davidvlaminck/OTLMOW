# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOverlangsemarkeringType(KeuzelijstField):
    """Mogelijke types van de overlangse markering."""
    naam = 'KlOverlangsemarkeringType'
    label = 'Overlangse markering type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOverlangsemarkeringType'
    definition = 'Mogelijke types van de overlangse markering.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOverlangsemarkeringType'
    options = {
        'doorlopend': KeuzelijstWaarde(invulwaarde='doorlopend',
                                       label='doorlopend',
                                       status='ingebruik',
                                       definitie='Een overlangse markering bestaande uit een doorlopende streep.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangsemarkeringType/doorlopend'),
        'onderbroken': KeuzelijstWaarde(invulwaarde='onderbroken',
                                        label='onderbroken',
                                        status='ingebruik',
                                        definitie='Een overlangse markering bestaande uit een onderbroken streep.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangsemarkeringType/onderbroken')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlOverlangsemarkeringType.get_dummy_data()

