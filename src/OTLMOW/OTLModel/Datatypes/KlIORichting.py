# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIORichting(KeuzelijstField):
    """Geeft aan of de IO-kaart dient voor input of output."""
    naam = 'KlIORichting'
    label = 'IO richting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIORichting'
    definition = 'Geeft aan of de IO-kaart dient voor input of output.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIORichting'
    options = {
        'input': KeuzelijstWaarde(invulwaarde='input',
                                  label='input',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIORichting/input'),
        'output': KeuzelijstWaarde(invulwaarde='output',
                                   label='output',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIORichting/output')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlIORichting.get_dummy_data()

