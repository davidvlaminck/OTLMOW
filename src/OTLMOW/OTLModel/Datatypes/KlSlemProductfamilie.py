# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSlemProductfamilie(KeuzelijstField):
    """De mogelijke productfamiles."""
    naam = 'KlSlemProductfamilie'
    label = 'Productfamilies'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSlemProductfamilie'
    definition = 'De mogelijke productfamiles.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSlemProductfamilie'
    options = {
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='1',
                              definitie='Productfamilie 1',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemProductfamilie/1'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='2',
                              definitie='Productfamilie 2',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemProductfamilie/2'),
        '5': KeuzelijstWaarde(invulwaarde='5',
                              label='5',
                              definitie='Productfamilie 5',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemProductfamilie/5'),
        '6': KeuzelijstWaarde(invulwaarde='6',
                              label='6',
                              definitie='Productfamilie 6',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlemProductfamilie/6')
    }

