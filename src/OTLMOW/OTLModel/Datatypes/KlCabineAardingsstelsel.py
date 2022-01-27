# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCabineAardingsstelsel(KeuzelijstField):
    """Lijst van mogelijke aardinggsstelsels."""
    naam = 'KlCabineAardingsstelsel'
    label = 'Cabine aardingsstelsel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCabineAardingsstelsel'
    definition = 'Lijst van mogelijke aardinggsstelsels.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCabineAardingsstelsel'
    options = {
        'gescheiden': KeuzelijstWaarde(invulwaarde='gescheiden',
                                       label='gescheiden',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineAardingsstelsel/gescheiden'),
        'globaal': KeuzelijstWaarde(invulwaarde='globaal',
                                    label='globaal',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineAardingsstelsel/globaal')
    }

