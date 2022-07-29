# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCalamiteitsbordType(KeuzelijstField):
    """Types van calamiteitsbord."""
    naam = 'KlCalamiteitsbordType'
    label = 'Calamiteitsbord type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCalamiteitsbordType'
    definition = 'Types van calamiteitsbord.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCalamiteitsbordType'
    options = {
        'draaiend-bord': KeuzelijstWaarde(invulwaarde='draaiend-bord',
                                          label='draaiend bord',
                                          status='ingebruik',
                                          definitie='Een draaiend calamiteitsbord.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCalamiteitsbordType/draaiend-bord'),
        'dragend-bord': KeuzelijstWaarde(invulwaarde='dragend-bord',
                                         label='dragend bord',
                                         status='ingebruik',
                                         definitie='Een dragend calamiteitsbord.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCalamiteitsbordType/dragend-bord')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

