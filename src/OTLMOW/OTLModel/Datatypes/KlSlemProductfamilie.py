# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSlemProductfamilie(KeuzelijstField):
    """De mogelijke productfamiles."""
    naam = 'KlSlemProductfamilie'
    label = 'Productfamilies'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSlemProductfamilie'
    definition = 'De mogelijke productfamiles.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSlemProductfamilie'
    options = {
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='1',
                              status='ingebruik',
                              definitie='Productfamilie 1',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemProductfamilie/1'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='2',
                              status='ingebruik',
                              definitie='Productfamilie 2',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemProductfamilie/2'),
        '5': KeuzelijstWaarde(invulwaarde='5',
                              label='5',
                              status='ingebruik',
                              definitie='Productfamilie 5',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemProductfamilie/5'),
        '6': KeuzelijstWaarde(invulwaarde='6',
                              label='6',
                              status='ingebruik',
                              definitie='Productfamilie 6',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemProductfamilie/6')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

