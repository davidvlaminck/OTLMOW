# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBrandblusserBlusmiddel(KeuzelijstField):
    """Keuzelijst met de verschillende mogelijke blusmiddelen voor een brandblusser."""
    naam = 'KlBrandblusserBlusmiddel'
    label = 'Brandblusser blusmiddel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBrandblusserBlusmiddel'
    definition = 'Keuzelijst met de verschillende mogelijke blusmiddelen voor een brandblusser.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBrandblusserBlusmiddel'
    options = {
        'poeder': KeuzelijstWaarde(invulwaarde='poeder',
                                   label='poeder',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserBlusmiddel/poeder'),
        'schuim': KeuzelijstWaarde(invulwaarde='schuim',
                                   label='schuim',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserBlusmiddel/schuim')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBrandblusserBlusmiddel.get_dummy_data()

