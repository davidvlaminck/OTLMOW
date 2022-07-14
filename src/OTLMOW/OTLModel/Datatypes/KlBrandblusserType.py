# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBrandblusserType(KeuzelijstField):
    """Keuzelijst met verschillende types van brandblussers volgens de algemene classificatie van brandblussers."""
    naam = 'KlBrandblusserType'
    label = 'Brandblusser type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBrandblusserType'
    definition = 'Keuzelijst met verschillende types van brandblussers volgens de algemene classificatie van brandblussers.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBrandblusserType'
    options = {
        'a': KeuzelijstWaarde(invulwaarde='a',
                              label='a',
                              status='ingebruik',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserType/a'),
        'b': KeuzelijstWaarde(invulwaarde='b',
                              label='b',
                              status='ingebruik',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserType/b'),
        'c': KeuzelijstWaarde(invulwaarde='c',
                              label='c',
                              status='ingebruik',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserType/c'),
        'd': KeuzelijstWaarde(invulwaarde='d',
                              label='d',
                              status='ingebruik',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserType/d')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

