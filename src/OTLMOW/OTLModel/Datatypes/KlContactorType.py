# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlContactorType(KeuzelijstField):
    """Geeft aan of het een K of Q contactor betreft."""
    naam = 'KlContactorType'
    label = 'contactor type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlContactorType'
    definition = 'Geeft aan of het een K of Q contactor betreft.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlContactorType'
    options = {
        'K': KeuzelijstWaarde(invulwaarde='K',
                              label='K',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlContactorType/K'),
        'Q': KeuzelijstWaarde(invulwaarde='Q',
                              label='Q',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlContactorType/Q')
    }

