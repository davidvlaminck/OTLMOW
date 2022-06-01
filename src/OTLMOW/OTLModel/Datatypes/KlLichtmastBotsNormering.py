# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLichtmastBotsNormering(KeuzelijstField):
    """Lijst van mogelijke waarden voor botsnormering van lichtmasten."""
    naam = 'KlLichtmastBotsNormering'
    label = 'Lichtmast botsnormering'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLichtmastBotsNormering'
    definition = 'Lijst van mogelijke waarden voor botsnormering van lichtmasten.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLichtmastBotsNormering'
    options = {
        '100HE1': KeuzelijstWaarde(invulwaarde='100HE1',
                                   label='100HE1',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/100HE1'),
        '100HE2': KeuzelijstWaarde(invulwaarde='100HE2',
                                   label='100HE2',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/100HE2'),
        '100HE3': KeuzelijstWaarde(invulwaarde='100HE3',
                                   label='100HE3',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/100HE3'),
        '100LE1': KeuzelijstWaarde(invulwaarde='100LE1',
                                   label='100LE1',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/100LE1'),
        '100LE2': KeuzelijstWaarde(invulwaarde='100LE2',
                                   label='100LE2',
                                   definitie='nader in te vullen',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/100LE2'),
        '100LE3': KeuzelijstWaarde(invulwaarde='100LE3',
                                   label='100LE3',
                                   definitie='nader in te vullen',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/100LE3'),
        '100NE1': KeuzelijstWaarde(invulwaarde='100NE1',
                                   label='100NE1',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/100NE1'),
        '100NE2': KeuzelijstWaarde(invulwaarde='100NE2',
                                   label='100NE2',
                                   definitie='nader in te vullen',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/100NE2'),
        '100NE4': KeuzelijstWaarde(invulwaarde='100NE4',
                                   label='100NE4',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/100NE4'),
        '50HE1': KeuzelijstWaarde(invulwaarde='50HE1',
                                  label='50HE1',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/50HE1'),
        '50HE2': KeuzelijstWaarde(invulwaarde='50HE2',
                                  label='50HE2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/50HE2'),
        '50HE3': KeuzelijstWaarde(invulwaarde='50HE3',
                                  label='50HE3',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/50HE3'),
        '50LE1': KeuzelijstWaarde(invulwaarde='50LE1',
                                  label='50LE1',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/50LE1'),
        '50LE2': KeuzelijstWaarde(invulwaarde='50LE2',
                                  label='50LE2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/50LE2'),
        '50LE3': KeuzelijstWaarde(invulwaarde='50LE3',
                                  label='50LE3',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/50LE3'),
        '50NE1': KeuzelijstWaarde(invulwaarde='50NE1',
                                  label='50NE1',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/50NE1'),
        '50NE2': KeuzelijstWaarde(invulwaarde='50NE2',
                                  label='50NE2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/50NE2'),
        '50NE3': KeuzelijstWaarde(invulwaarde='50NE3',
                                  label='50NE3',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/50NE3'),
        '50NE4': KeuzelijstWaarde(invulwaarde='50NE4',
                                  label='50NE4',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/50NE4'),
        '70HE1': KeuzelijstWaarde(invulwaarde='70HE1',
                                  label='70HE1',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/70HE1'),
        '70HE2': KeuzelijstWaarde(invulwaarde='70HE2',
                                  label='70HE2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/70HE2'),
        '70HE3': KeuzelijstWaarde(invulwaarde='70HE3',
                                  label='70HE3',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/70HE3'),
        '70LE1': KeuzelijstWaarde(invulwaarde='70LE1',
                                  label='70LE1',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/70LE1'),
        '70LE2': KeuzelijstWaarde(invulwaarde='70LE2',
                                  label='70LE2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/70LE2'),
        '70LE3': KeuzelijstWaarde(invulwaarde='70LE3',
                                  label='70LE3',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/70LE3'),
        '70NE1': KeuzelijstWaarde(invulwaarde='70NE1',
                                  label='70NE1',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/70NE1'),
        '70NE2': KeuzelijstWaarde(invulwaarde='70NE2',
                                  label='70NE2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/70NE2'),
        '70NE3': KeuzelijstWaarde(invulwaarde='70NE3',
                                  label='70NE3',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/70NE3'),
        '70NE4': KeuzelijstWaarde(invulwaarde='70NE4',
                                  label='70NE4',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/70NE4'),
        '9': KeuzelijstWaarde(invulwaarde='9',
                              label='9',
                              definitie='nader in te vullen',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/9'),
        'niet-botsvriendelijke-mast': KeuzelijstWaarde(invulwaarde='niet-botsvriendelijke-mast',
                                                       label='Niet-botsvriendelijke mast',
                                                       definitie='Mast heeft geen botsvriendelijke normering.',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastBotsNormering/niet-botsvriendelijke-mast')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlLichtmastBotsNormering.get_dummy_data()

