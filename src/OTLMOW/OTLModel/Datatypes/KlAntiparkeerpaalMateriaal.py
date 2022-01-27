# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAntiparkeerpaalMateriaal(KeuzelijstField):
    """Bepaling van het vervaardigingsmateriaal van de antiparkeerpaal."""
    naam = 'KlAntiparkeerpaalMateriaal'
    label = 'Antiparkeerpaal materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAntiparkeerpaalMateriaal'
    definition = 'Bepaling van het vervaardigingsmateriaal van de antiparkeerpaal.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAntiparkeerpaalMateriaal'
    options = {
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='hout',
                                 definitie='Keuze hout voor het antiparkeerpaal materiaal.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAntiparkeerpaalMateriaal/hout'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='kunststof',
                                      definitie='Keuze kunststof voor het antiparkeerpaal materiaal.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAntiparkeerpaalMateriaal/kunststof'),
        'metaal': KeuzelijstWaarde(invulwaarde='metaal',
                                   label='metaal',
                                   definitie='Keuze metaal voor het antiparkeerpaal materiaal.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAntiparkeerpaalMateriaal/metaal')
    }

