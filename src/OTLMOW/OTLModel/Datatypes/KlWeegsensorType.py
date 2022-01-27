# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWeegsensorType(KeuzelijstField):
    """Het type van de weegsensor."""
    naam = 'KlWeegsensorType'
    label = 'Weegsensor type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeegsensorType'
    definition = 'Het type van de weegsensor.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeegsensorType'
    options = {
        'piëzo-kwarts': KeuzelijstWaarde(invulwaarde='piëzo-kwarts',
                                         label='piëzo-kwarts',
                                         definitie='piëzo-kwarts',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeegsensorType/piëzo-kwarts')
    }

