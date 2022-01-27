# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVoorschakelapparaatType(KeuzelijstField):
    """Type van het voorschakelapparaat."""
    naam = 'KlVoorschakelapparaatType'
    label = 'Voorschakelapparaat type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVoorschakelapparaatType'
    definition = 'Type van het voorschakelapparaat.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVoorschakelapparaatType'
    options = {
        'elektromechanisch': KeuzelijstWaarde(invulwaarde='elektromechanisch',
                                              label='elektromechanisch',
                                              definitie='/ CLASS : IVSB',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoorschakelapparaatType/elektromechanisch'),
        'elektronisch': KeuzelijstWaarde(invulwaarde='elektronisch',
                                         label='elektronisch',
                                         definitie='/ CLASS : IVSB',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoorschakelapparaatType/elektronisch')
    }

