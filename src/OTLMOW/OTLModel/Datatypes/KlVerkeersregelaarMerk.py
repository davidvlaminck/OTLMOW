# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersregelaarMerk(KeuzelijstField):
    """Keuzelijst met merknamen voor Verkeersregelaar."""
    naam = 'KlVerkeersregelaarMerk'
    label = 'verkeersregelaar merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersregelaarMerk'
    definition = 'Keuzelijst met merknamen voor Verkeersregelaar.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersregelaarMerk'
    options = {
        'dynniq': KeuzelijstWaarde(invulwaarde='dynniq',
                                   label='Dynniq',
                                   definitie='Dynniq',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarMerk/dynniq'),
        'ko-hartog': KeuzelijstWaarde(invulwaarde='ko-hartog',
                                      label='Ko Hartog',
                                      definitie='Ko Hartog',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarMerk/ko-hartog'),
        'peek': KeuzelijstWaarde(invulwaarde='peek',
                                 label='Peek',
                                 definitie='Peek',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarMerk/peek'),
        'siemens': KeuzelijstWaarde(invulwaarde='siemens',
                                    label='Siemens',
                                    definitie='Siemens',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarMerk/siemens'),
        'swarco': KeuzelijstWaarde(invulwaarde='swarco',
                                   label='Swarco',
                                   definitie='Swarco (voorheen Dynniq)',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarMerk/swarco')
    }

