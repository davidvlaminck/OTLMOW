# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfmetingsensorModelnaam(KeuzelijstField):
    """De modelnaam van de afmetingsensor."""
    naam = 'KlAfmetingsensorModelnaam'
    label = 'Afmetingsensor modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfmetingsensorModelnaam'
    definition = 'De modelnaam van de afmetingsensor.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfmetingsensorModelnaam'
    options = {
        'FPS': KeuzelijstWaarde(invulwaarde='FPS',
                                label='FPS',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfmetingsensorModelnaam/FPS'),
        'LMS': KeuzelijstWaarde(invulwaarde='LMS',
                                label='LMS',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfmetingsensorModelnaam/LMS')
    }

