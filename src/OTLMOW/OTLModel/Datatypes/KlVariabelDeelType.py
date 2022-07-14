# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVariabelDeelType(KeuzelijstField):
    """Types van het variabel deel van een overstortrand."""
    naam = 'KlVariabelDeelType'
    label = 'Variabel deel type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVariabelDeelType'
    definition = 'Types van het variabel deel van een overstortrand.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVariabelDeelType'
    options = {
        'overstortplaat': KeuzelijstWaarde(invulwaarde='overstortplaat',
                                           label='overstortplaat',
                                           status='ingebruik',
                                           definitie='overstortplaat',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVariabelDeelType/overstortplaat'),
        'schotbalk': KeuzelijstWaarde(invulwaarde='schotbalk',
                                      label='schotbalk',
                                      status='ingebruik',
                                      definitie='schotbalk',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVariabelDeelType/schotbalk')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

