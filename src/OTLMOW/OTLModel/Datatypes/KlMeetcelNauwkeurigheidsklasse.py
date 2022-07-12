# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMeetcelNauwkeurigheidsklasse(KeuzelijstField):
    """Nauwkeurigheidsklasse van de meetcel (vb 0,2; 0,2s; 0,5; ...)."""
    naam = 'KlMeetcelNauwkeurigheidsklasse'
    label = 'Meetcel nauwkeurigheidsklasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMeetcelNauwkeurigheidsklasse'
    definition = 'Nauwkeurigheidsklasse van de meetcel (vb 0,2; 0,2s; 0,5; ...).'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMeetcelNauwkeurigheidsklasse'
    options = {
        '0.2': KeuzelijstWaarde(invulwaarde='0.2',
                                label='0.2',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeetcelNauwkeurigheidsklasse/0.2'),
        '0.2-S': KeuzelijstWaarde(invulwaarde='0.2-S',
                                  label='0.2 S',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeetcelNauwkeurigheidsklasse/0.2-S'),
        '0.5': KeuzelijstWaarde(invulwaarde='0.5',
                                label='0.5',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeetcelNauwkeurigheidsklasse/0.5')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlMeetcelNauwkeurigheidsklasse.get_dummy_data()

