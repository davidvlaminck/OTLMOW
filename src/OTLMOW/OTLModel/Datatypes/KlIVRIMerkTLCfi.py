# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIMerkTLCfi(KeuzelijstField):
    """Het merk van de TLC-fi poort."""
    naam = 'KlIVRIMerkTLCfi'
    label = 'iVRIMerkTLCfi'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIVRIMerkTLCfi'
    definition = 'Het merk van de TLC-fi poort.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIMerkTLCfi'
    options = {
        'dynniq': KeuzelijstWaarde(invulwaarde='dynniq',
                                   label='Dynniq',
                                   status='ingebruik',
                                   definitie='Dynniq',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIMerkTLCfi/dynniq'),
        'ko-hartog': KeuzelijstWaarde(invulwaarde='ko-hartog',
                                      label='Ko Hartog',
                                      status='ingebruik',
                                      definitie='Ko Hartog',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIMerkTLCfi/ko-hartog'),
        'siemens': KeuzelijstWaarde(invulwaarde='siemens',
                                    label='Siemens',
                                    status='ingebruik',
                                    definitie='Siemens',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIMerkTLCfi/siemens'),
        'swarco': KeuzelijstWaarde(invulwaarde='swarco',
                                   label='Swarco',
                                   status='ingebruik',
                                   definitie='Swarco (voorheen Dynniq)',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIMerkTLCfi/swarco'),
        'yunex': KeuzelijstWaarde(invulwaarde='yunex',
                                  label='Yunex',
                                  status='ingebruik',
                                  definitie='Yunex',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIMerkTLCfi/yunex')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

