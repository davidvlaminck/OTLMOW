# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVariabelDeelType(KeuzelijstField):
    """Types van het variabel deel van een overstortrand."""
    naam = 'KlVariabelDeelType'
    label = 'Variabel deel type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVariabelDeelType'
    definition = 'Types van het variabel deel van een overstortrand.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVariabelDeelType'
    options = {
        'overstortplaat': KeuzelijstWaarde(invulwaarde='overstortplaat',
                                           label='overstortplaat',
                                           definitie='overstortplaat',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVariabelDeelType/overstortplaat'),
        'schotbalk': KeuzelijstWaarde(invulwaarde='schotbalk',
                                      label='schotbalk',
                                      definitie='schotbalk',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVariabelDeelType/schotbalk')
    }

