# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCalamiteitsbordType(KeuzelijstField):
    """Types van calamiteitsbord."""
    naam = 'KlCalamiteitsbordType'
    label = 'Calamiteitsbord type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCalamiteitsbordType'
    definition = 'Types van calamiteitsbord.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCalamiteitsbordType'
    options = {
        'draaiend-bord': KeuzelijstWaarde(invulwaarde='draaiend-bord',
                                          label='draaiend bord',
                                          definitie='Een draaiend calamiteitsbord.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCalamiteitsbordType/draaiend-bord'),
        'dragend-bord': KeuzelijstWaarde(invulwaarde='dragend-bord',
                                         label='dragend bord',
                                         definitie='Een dragend calamiteitsbord.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCalamiteitsbordType/dragend-bord')
    }

