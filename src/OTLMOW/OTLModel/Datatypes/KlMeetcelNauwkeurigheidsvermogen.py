# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMeetcelNauwkeurigheidsvermogen(KeuzelijstField):
    """Nauwkeurigheidsvermogen van de meetcel in voltampère (bv. 5 of 15)."""
    naam = 'KlMeetcelNauwkeurigheidsvermogen'
    label = 'Meetcel nauwkeurigheidsvermogen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMeetcelNauwkeurigheidsvermogen'
    definition = 'Nauwkeurigheidsvermogen van de meetcel in voltampère (bv. 5 of 15).'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMeetcelNauwkeurigheidsvermogen'
    options = {
        '15': KeuzelijstWaarde(invulwaarde='15',
                               label='15',
                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeetcelNauwkeurigheidsvermogen/15'),
        '5': KeuzelijstWaarde(invulwaarde='5',
                              label='5',
                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeetcelNauwkeurigheidsvermogen/5')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlMeetcelNauwkeurigheidsvermogen.get_dummy_data()

