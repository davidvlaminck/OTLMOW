# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMIVLusUitslijprichting(KeuzelijstField):
    """De uitlopers van de lus gaan naar links of naar rechts  bekeken ten opzichte van de rijrichting."""
    naam = 'KlMIVLusUitslijprichting'
    label = 'MIV-lus uitslijprichting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMIVLusUitslijprichting'
    definition = 'De uitlopers van de lus gaan naar links of naar rechts  bekeken ten opzichte van de rijrichting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMIVLusUitslijprichting'
    options = {
        'links': KeuzelijstWaarde(invulwaarde='links',
                                  label='links',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVLusUitslijprichting/links'),
        'rechts': KeuzelijstWaarde(invulwaarde='rechts',
                                   label='rechts',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVLusUitslijprichting/rechts')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

