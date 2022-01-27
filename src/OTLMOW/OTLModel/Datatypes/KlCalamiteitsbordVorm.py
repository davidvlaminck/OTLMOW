# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCalamiteitsbordVorm(KeuzelijstField):
    """Vormen van het calamiteitsbord."""
    naam = 'KlCalamiteitsbordVorm'
    label = 'Calamiteitsbord vorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCalamiteitsbordVorm'
    definition = 'Vormen van het calamiteitsbord.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCalamiteitsbordVorm'
    options = {
        'rechthoekig': KeuzelijstWaarde(invulwaarde='rechthoekig',
                                        label='rechthoekig',
                                        definitie='Een rechthoekig calamiteitsbord.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCalamiteitsbordVorm/rechthoekig'),
        'ruitvormig': KeuzelijstWaarde(invulwaarde='ruitvormig',
                                       label='ruitvormig',
                                       definitie='Een ruitvormig calamiteitsbord.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCalamiteitsbordVorm/ruitvormig')
    }

