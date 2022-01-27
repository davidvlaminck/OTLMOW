# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBestrijkingKaliber(KeuzelijstField):
    """De mogelijke kalibers."""
    naam = 'KlBestrijkingKaliber'
    label = 'kalibers'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBestrijkingKaliber'
    definition = 'De mogelijke kalibers.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBestrijkingKaliber'
    options = {
        '2-10': KeuzelijstWaarde(invulwaarde='2-10',
                                 label='2/10',
                                 definitie='kaliber 2/10',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingKaliber/2-10'),
        '2-4': KeuzelijstWaarde(invulwaarde='2-4',
                                label='2/4',
                                definitie='kaliber 2/4',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingKaliber/2-4'),
        '2-6.3': KeuzelijstWaarde(invulwaarde='2-6.3',
                                  label='2/6.3',
                                  definitie='kaliber 2/6.3',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingKaliber/2-6.3'),
        '4-10': KeuzelijstWaarde(invulwaarde='4-10',
                                 label='4/10',
                                 definitie='kaliber 4/10',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingKaliber/4-10'),
        '4-6.3': KeuzelijstWaarde(invulwaarde='4-6.3',
                                  label='4/6.3',
                                  definitie='kaliber 4/6.3',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingKaliber/4-6.3'),
        '6.3-10': KeuzelijstWaarde(invulwaarde='6.3-10',
                                   label='6.3/10',
                                   definitie='kaliber 6.3/10',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingKaliber/6.3-10')
    }

