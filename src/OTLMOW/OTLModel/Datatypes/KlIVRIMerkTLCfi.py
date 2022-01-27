# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIMerkTLCfi(KeuzelijstField):
    """Het merk van de TLC-fi poort."""
    naam = 'KlIVRIMerkTLCfi'
    label = 'iVRIMerkTLCfi'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIVRIMerkTLCfi'
    definition = 'Het merk van de TLC-fi poort.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIMerkTLCfi'
    options = {
        'dynniq': KeuzelijstWaarde(invulwaarde='dynniq',
                                   label='Dynniq',
                                   definitie='Dynniq',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIMerkTLCfi/dynniq'),
        'ko-hartog': KeuzelijstWaarde(invulwaarde='ko-hartog',
                                      label='Ko Hartog',
                                      definitie='Ko Hartog',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIMerkTLCfi/ko-hartog'),
        'siemens': KeuzelijstWaarde(invulwaarde='siemens',
                                    label='Siemens',
                                    definitie='Siemens',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIMerkTLCfi/siemens'),
        'yunex': KeuzelijstWaarde(invulwaarde='yunex',
                                  label='Yunex',
                                  definitie='Yunex',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIMerkTLCfi/yunex')
    }

