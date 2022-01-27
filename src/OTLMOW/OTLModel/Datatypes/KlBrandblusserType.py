# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBrandblusserType(KeuzelijstField):
    """Keuzelijst met verschillende types van brandblussers volgens de algemene classificatie van brandblussers."""
    naam = 'KlBrandblusserType'
    label = 'Brandblusser type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBrandblusserType'
    definition = 'Keuzelijst met verschillende types van brandblussers volgens de algemene classificatie van brandblussers.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBrandblusserType'
    options = {
        'a': KeuzelijstWaarde(invulwaarde='a',
                              label='a',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserType/a'),
        'b': KeuzelijstWaarde(invulwaarde='b',
                              label='b',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserType/b'),
        'c': KeuzelijstWaarde(invulwaarde='c',
                              label='c',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserType/c'),
        'd': KeuzelijstWaarde(invulwaarde='d',
                              label='d',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserType/d')
    }

