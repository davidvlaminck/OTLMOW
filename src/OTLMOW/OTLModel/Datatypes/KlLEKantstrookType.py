# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEKantstrookType(KeuzelijstField):
    """Types van kantstrook."""
    naam = 'KlLEKantstrookType'
    label = 'Kantstrook type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEKantstrookType'
    definition = 'Types van kantstrook.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEKantstrookType'
    options = {
        'type-II-A-1': KeuzelijstWaarde(invulwaarde='type-II-A-1',
                                        label='type II A 1',
                                        definitie='type II A 1',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantstrookType/type-II-A-1'),
        'type-II-B-1': KeuzelijstWaarde(invulwaarde='type-II-B-1',
                                        label='type II B 1',
                                        definitie='type II B 1',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantstrookType/type-II-B-1'),
        'type-II-C-1': KeuzelijstWaarde(invulwaarde='type-II-C-1',
                                        label='type II C 1',
                                        definitie='type II C 1',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantstrookType/type-II-C-1'),
        'type-II-D-1': KeuzelijstWaarde(invulwaarde='type-II-D-1',
                                        label='type II D 1',
                                        definitie='type II D 1',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantstrookType/type-II-D-1'),
        'type-II-E-1': KeuzelijstWaarde(invulwaarde='type-II-E-1',
                                        label='type II E 1',
                                        definitie='type II E 1',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantstrookType/type-II-E-1')
    }

