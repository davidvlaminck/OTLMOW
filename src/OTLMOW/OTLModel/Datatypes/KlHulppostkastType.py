# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHulppostkastType(KeuzelijstField):
    """Lijst met al dan niet gestandaardiseerde types voor hulppostkasten."""
    naam = 'KlHulppostkastType'
    label = 'Hulppostkast type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHulppostkastType'
    definition = 'Lijst met al dan niet gestandaardiseerde types voor hulppostkasten.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHulppostkastType'
    options = {
        'a': KeuzelijstWaarde(invulwaarde='a',
                              label='a',
                              status='ingebruik',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulppostkastType/a'),
        'c': KeuzelijstWaarde(invulwaarde='c',
                              label='c',
                              status='ingebruik',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulppostkastType/c')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

