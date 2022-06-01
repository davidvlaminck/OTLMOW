# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPositieSoort(KeuzelijstField):
    """Posities van het wegdek."""
    naam = 'KlPositieSoort'
    label = 'Positie soort'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPositieSoort'
    definition = 'Posities van het wegdek.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPositieSoort'
    options = {
        'linkerrand': KeuzelijstWaarde(invulwaarde='linkerrand',
                                       label='linkerrand',
                                       definitie='linkerrand',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPositieSoort/linkerrand'),
        'midden': KeuzelijstWaarde(invulwaarde='midden',
                                   label='midden',
                                   definitie='midden',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPositieSoort/midden'),
        'rechterrand': KeuzelijstWaarde(invulwaarde='rechterrand',
                                        label='rechterrand',
                                        definitie='rechterrand',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPositieSoort/rechterrand')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlPositieSoort.get_dummy_data()

