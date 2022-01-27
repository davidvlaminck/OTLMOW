# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlANPRModelnaam(KeuzelijstField):
    """De modelnaam van de ANPR camera."""
    naam = 'KlANPRModelnaam'
    label = 'ANPR modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlANPRModelnaam'
    definition = 'De modelnaam van de ANPR camera.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlANPRModelnaam'
    options = {
        'G1': KeuzelijstWaarde(invulwaarde='G1',
                               label='G1',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRModelnaam/G1'),
        'G3': KeuzelijstWaarde(invulwaarde='G3',
                               label='G3',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRModelnaam/G3'),
        'dual': KeuzelijstWaarde(invulwaarde='dual',
                                 label='dual',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRModelnaam/dual'),
        'i-car-cam5': KeuzelijstWaarde(invulwaarde='i-car-cam5',
                                       label='iCar cam5',
                                       definitie='iCar cam5',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRModelnaam/i-car-cam5')
    }

