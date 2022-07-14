# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLichtmastMasthoogte(KeuzelijstField):
    """De standaard masthoogten."""
    naam = 'KlLichtmastMasthoogte'
    label = 'Wv masthoogte'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLichtmastMasthoogte'
    definition = 'De standaard masthoogten.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLichtmastMasthoogte'
    options = {
        '10.00': KeuzelijstWaarde(invulwaarde='10.00',
                                  label='10.00',
                                  status='ingebruik',
                                  definitie='Lijst paalhoogtes/ CLASS : VPLMAST',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasthoogte/10.00'),
        '12.00': KeuzelijstWaarde(invulwaarde='12.00',
                                  label='12.00',
                                  status='ingebruik',
                                  definitie='Lijst paalhoogtes/ CLASS : VPLMAST',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasthoogte/12.00'),
        '12.50': KeuzelijstWaarde(invulwaarde='12.50',
                                  label='12.50',
                                  status='ingebruik',
                                  definitie='Lijst paalhoogtes/ CLASS : VPLMAST',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasthoogte/12.50'),
        '16.00': KeuzelijstWaarde(invulwaarde='16.00',
                                  label='16.00',
                                  status='ingebruik',
                                  definitie='Lijst paalhoogtes/ CLASS : VPLMAST',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasthoogte/16.00'),
        '18.00': KeuzelijstWaarde(invulwaarde='18.00',
                                  label='18.00',
                                  status='ingebruik',
                                  definitie='Lijst paalhoogtes/ CLASS : VPLMAST',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasthoogte/18.00'),
        '20.00': KeuzelijstWaarde(invulwaarde='20.00',
                                  label='20.00',
                                  status='ingebruik',
                                  definitie='Lijst paalhoogtes/ CLASS : VPLMAST',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasthoogte/20.00'),
        '3.20': KeuzelijstWaarde(invulwaarde='3.20',
                                 label='3.20',
                                 status='ingebruik',
                                 definitie='Lijst paalhoogtes/ CLASS : VPLMAST',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasthoogte/3.20'),
        '4.00': KeuzelijstWaarde(invulwaarde='4.00',
                                 label='4.00',
                                 status='ingebruik',
                                 definitie='Lijst paalhoogtes/ CLASS : VPLMAST',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasthoogte/4.00'),
        '5.00': KeuzelijstWaarde(invulwaarde='5.00',
                                 label='5.00',
                                 status='ingebruik',
                                 definitie='Lijst paalhoogtes/ CLASS : VPLMAST',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasthoogte/5.00'),
        '6.30': KeuzelijstWaarde(invulwaarde='6.30',
                                 label='6.30',
                                 status='ingebruik',
                                 definitie='Lijst paalhoogtes/ CLASS : VPLMAST',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasthoogte/6.30'),
        '8.00': KeuzelijstWaarde(invulwaarde='8.00',
                                 label='8.00',
                                 status='ingebruik',
                                 definitie='Lijst paalhoogtes/ CLASS : VPLMAST',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastMasthoogte/8.00')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

