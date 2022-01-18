# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMaaiFrequentie(KeuzelijstField):
    """Het aantal keer dat er gemaaid wordt per jaar."""
    naam = 'KlMaaiFrequentie'
    label = 'Maaifrequentie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlMaaiFrequentie'
    definition = 'Het aantal keer dat er gemaaid wordt per jaar.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMaaiFrequentie'
    options = {
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='1',
                              definitie='Eén keer per jaar maaien.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/1'),
        '1-2': KeuzelijstWaarde(invulwaarde='1-2',
                                label='1/2',
                                definitie='Eén keer om de twee jaar maaien.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/1-2'),
        '1-3': KeuzelijstWaarde(invulwaarde='1-3',
                                label='1/3',
                                definitie='Eén keer om de drie jaar maaien.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/1-3'),
        '10-15': KeuzelijstWaarde(invulwaarde='10-15',
                                  label='10-15',
                                  definitie='10 tot 15 keer per jaar maaien.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/10-15'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='2',
                              definitie='Twee keer per jaar maaien.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/2'),
        '3': KeuzelijstWaarde(invulwaarde='3',
                              label='3',
                              definitie='Drie keer per jaar maaien.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/3'),
        '4-6': KeuzelijstWaarde(invulwaarde='4-6',
                                label='4-6',
                                definitie='Vier tot zes keer per jaar maaien.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/4-6'),
        '7-9': KeuzelijstWaarde(invulwaarde='7-9',
                                label='7-9',
                                definitie='Zeven tot negen keer per jaar maaien.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/7-9')
    }

