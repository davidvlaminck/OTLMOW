# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMaaiFrequentie(KeuzelijstField):
    """Het aantal keer dat er gemaaid wordt per jaar."""
    naam = 'KlMaaiFrequentie'
    label = 'Maaifrequentie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlMaaiFrequentie'
    definition = 'Het aantal keer dat er gemaaid wordt per jaar.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMaaiFrequentie'
    options = {
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='1',
                              status='ingebruik',
                              definitie='Eén keer per jaar maaien.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/1'),
        '1-2': KeuzelijstWaarde(invulwaarde='1-2',
                                label='1/2',
                                status='ingebruik',
                                definitie='Eén keer om de twee jaar maaien.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/1-2'),
        '1-3': KeuzelijstWaarde(invulwaarde='1-3',
                                label='1/3',
                                status='ingebruik',
                                definitie='Eén keer om de drie jaar maaien.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/1-3'),
        '10-15': KeuzelijstWaarde(invulwaarde='10-15',
                                  label='10-15',
                                  status='ingebruik',
                                  definitie='10 tot 15 keer per jaar maaien.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/10-15'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='2',
                              status='ingebruik',
                              definitie='Twee keer per jaar maaien.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/2'),
        '3': KeuzelijstWaarde(invulwaarde='3',
                              label='3',
                              status='ingebruik',
                              definitie='Drie keer per jaar maaien.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/3'),
        '4-6': KeuzelijstWaarde(invulwaarde='4-6',
                                label='4-6',
                                status='ingebruik',
                                definitie='Vier tot zes keer per jaar maaien.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/4-6'),
        '7-9': KeuzelijstWaarde(invulwaarde='7-9',
                                label='7-9',
                                status='ingebruik',
                                definitie='Zeven tot negen keer per jaar maaien.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/7-9'),
        'minder-dan-1-3': KeuzelijstWaarde(invulwaarde='minder-dan-1-3',
                                           label='minder dan 1/3',
                                           status='ingebruik',
                                           definitie='Minder dan één keer om de drie jaar maaien.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiFrequentie/minder-dan-1-3')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

