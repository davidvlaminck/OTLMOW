# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCameraModelnaam(KeuzelijstField):
    """De modelnaam van de camera."""
    naam = 'KlCameraModelnaam'
    label = 'Camera modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCameraModelnaam'
    definition = 'De modelnaam van de camera.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCameraModelnaam'
    options = {
        'dinion-ip-starlight-8000-m': KeuzelijstWaarde(invulwaarde='dinion-ip-starlight-8000-m',
                                                       label='Dinion IP Starlight 8000 M',
                                                       definitie='Dinion IP Starlight 8000 M',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/dinion-ip-starlight-8000-m'),
        'ulisse-hd': KeuzelijstWaarde(invulwaarde='ulisse-hd',
                                      label='Ulisse HD',
                                      definitie='Ulisse HD',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/ulisse-hd')
    }

