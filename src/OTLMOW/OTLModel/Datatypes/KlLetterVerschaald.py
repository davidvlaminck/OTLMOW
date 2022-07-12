# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLetterVerschaald(KeuzelijstField):
    """De mogelijke letters voor een verschaalde lettermarkering."""
    naam = 'KlLetterVerschaald'
    label = 'Letter verschaald'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLetterVerschaald'
    definition = 'De mogelijke letters voor een verschaalde lettermarkering.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLetterVerschaald'
    options = {
        'A': KeuzelijstWaarde(invulwaarde='A',
                              label='A',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter A.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/A'),
        'B': KeuzelijstWaarde(invulwaarde='B',
                              label='B',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter B.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/B'),
        'C': KeuzelijstWaarde(invulwaarde='C',
                              label='C',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter C.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/C'),
        'D': KeuzelijstWaarde(invulwaarde='D',
                              label='D',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter D.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/D'),
        'E': KeuzelijstWaarde(invulwaarde='E',
                              label='E',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter E.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/E'),
        'F': KeuzelijstWaarde(invulwaarde='F',
                              label='F',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter F.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/F'),
        'G': KeuzelijstWaarde(invulwaarde='G',
                              label='G',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter G.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/G'),
        'H': KeuzelijstWaarde(invulwaarde='H',
                              label='H',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter H.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/H'),
        'I': KeuzelijstWaarde(invulwaarde='I',
                              label='I',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter I.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/I'),
        'J': KeuzelijstWaarde(invulwaarde='J',
                              label='J',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter J.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/J'),
        'K': KeuzelijstWaarde(invulwaarde='K',
                              label='K',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter K.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/K'),
        'L': KeuzelijstWaarde(invulwaarde='L',
                              label='L',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter L.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/L'),
        'M': KeuzelijstWaarde(invulwaarde='M',
                              label='M',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter M.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/M'),
        'N': KeuzelijstWaarde(invulwaarde='N',
                              label='N',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter N.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/N'),
        'O': KeuzelijstWaarde(invulwaarde='O',
                              label='O',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter O.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/O'),
        'P': KeuzelijstWaarde(invulwaarde='P',
                              label='P',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter P.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/P'),
        'Q': KeuzelijstWaarde(invulwaarde='Q',
                              label='Q',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter Q.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/Q'),
        'R': KeuzelijstWaarde(invulwaarde='R',
                              label='R',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter R.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/R'),
        'S': KeuzelijstWaarde(invulwaarde='S',
                              label='S',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter S.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/S'),
        'T': KeuzelijstWaarde(invulwaarde='T',
                              label='T',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter T.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/T'),
        'U': KeuzelijstWaarde(invulwaarde='U',
                              label='U',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter U.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/U'),
        'V': KeuzelijstWaarde(invulwaarde='V',
                              label='V',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter V.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/V'),
        'W': KeuzelijstWaarde(invulwaarde='W',
                              label='W',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter W.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/W'),
        'X': KeuzelijstWaarde(invulwaarde='X',
                              label='X',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter X.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/X'),
        'Y': KeuzelijstWaarde(invulwaarde='Y',
                              label='Y',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter Y.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/Y'),
        'Z': KeuzelijstWaarde(invulwaarde='Z',
                              label='Z',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Letter Z.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaald/Z')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlLetterVerschaald.get_dummy_data()

