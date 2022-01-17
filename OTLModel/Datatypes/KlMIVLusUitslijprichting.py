# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMIVLusUitslijprichting(KeuzelijstField):
    """De uitlopers van de lus gaan naar links of naar rechts  bekeken ten opzichte van de rijrichting."""
    naam = 'KlMIVLusUitslijprichting'
    label = 'MIV-lus uitslijprichting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMIVLusUitslijprichting'
    definition = 'De uitlopers van de lus gaan naar links of naar rechts  bekeken ten opzichte van de rijrichting.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMIVLusUitslijprichting'
    options = {
        'links': KeuzelijstWaarde(invulwaarde='links',
                                  label='links',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVLusUitslijprichting/links'),
        'rechts': KeuzelijstWaarde(invulwaarde='rechts',
                                   label='rechts',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVLusUitslijprichting/rechts')
    }

