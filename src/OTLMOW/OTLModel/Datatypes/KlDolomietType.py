# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDolomietType(KeuzelijstField):
    """Types van dolomiet."""
    naam = 'KlDolomietType'
    label = 'Dolomiet type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDolomietType'
    definition = 'Types van dolomiet.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDolomietType'
    options = {
        '0-15': KeuzelijstWaarde(invulwaarde='0-15',
                                 label='0-15',
                                 definitie='0/15',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDolomietType/0-15'),
        '0-5': KeuzelijstWaarde(invulwaarde='0-5',
                                label='0-5',
                                definitie='0/5',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDolomietType/0-5'),
        '5-15': KeuzelijstWaarde(invulwaarde='5-15',
                                 label='5-15',
                                 definitie='mei-15',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDolomietType/5-15')
    }

