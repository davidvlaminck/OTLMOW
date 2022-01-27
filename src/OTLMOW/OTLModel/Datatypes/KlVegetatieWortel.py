# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVegetatieWortel(KeuzelijstField):
    """De verschillende opties van hoe de wortel was bij aanplanting."""
    naam = 'KlVegetatieWortel'
    label = 'Vegetatie wortel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVegetatieWortel'
    definition = 'De verschillende opties van hoe de wortel was bij aanplanting.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVegetatieWortel'
    options = {
        'container': KeuzelijstWaarde(invulwaarde='container',
                                      label='container',
                                      definitie='De wortels zitten in een container of pot bij aanlevering en aanplant.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieWortel/container'),
        'draadkluit': KeuzelijstWaarde(invulwaarde='draadkluit',
                                       label='draadkluit',
                                       definitie='De wortels zitten in een met draad ingebonden kluit aarde',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieWortel/draadkluit'),
        'kluit': KeuzelijstWaarde(invulwaarde='kluit',
                                  label='kluit',
                                  definitie='De wortels zijn omringd met aarde.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieWortel/kluit'),
        'naakt': KeuzelijstWaarde(invulwaarde='naakt',
                                  label='naakt',
                                  definitie='Wortels waarrond geen grond aanwezig is',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieWortel/naakt')
    }

