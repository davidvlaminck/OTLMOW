# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBestrijkingProductfamilie(KeuzelijstField):
    """De mogelijke productfamiles."""
    naam = 'KlBestrijkingProductfamilie'
    label = 'Productfamilies'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBestrijkingProductfamilie'
    definition = 'De mogelijke productfamiles.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBestrijkingProductfamilie'
    options = {
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='1',
                              status='ingebruik',
                              definitie='Productfamilie 1',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingProductfamilie/1'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='2',
                              status='ingebruik',
                              definitie='Productfamilie 2',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingProductfamilie/2'),
        '3': KeuzelijstWaarde(invulwaarde='3',
                              label='3',
                              status='ingebruik',
                              definitie='Productfamilie 3',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingProductfamilie/3'),
        '4': KeuzelijstWaarde(invulwaarde='4',
                              label='4',
                              status='ingebruik',
                              definitie='Productfamilie 4',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingProductfamilie/4'),
        '5': KeuzelijstWaarde(invulwaarde='5',
                              label='5',
                              status='ingebruik',
                              definitie='Productfamilie 5',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingProductfamilie/5'),
        '6': KeuzelijstWaarde(invulwaarde='6',
                              label='6',
                              status='ingebruik',
                              definitie='Productfamilie 6',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingProductfamilie/6'),
        '7': KeuzelijstWaarde(invulwaarde='7',
                              label='7',
                              status='ingebruik',
                              definitie='Productfamilie 7',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingProductfamilie/7'),
        '8': KeuzelijstWaarde(invulwaarde='8',
                              label='8',
                              status='ingebruik',
                              definitie='Productfamilie 8',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingProductfamilie/8')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

