# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBrandblusserGewicht(KeuzelijstField):
    """Keuzelijst met de mogelijke gewichten van brandblussers."""
    naam = 'KlBrandblusserGewicht'
    label = 'Brandblusser gewicht'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBrandblusserGewicht'
    definition = 'Keuzelijst met de mogelijke gewichten van brandblussers.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBrandblusserGewicht'
    options = {
        '6-kg': KeuzelijstWaarde(invulwaarde='6-kg',
                                 label='6 kg',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserGewicht/6-kg'),
        '9-kg': KeuzelijstWaarde(invulwaarde='9-kg',
                                 label='9 kg',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserGewicht/9-kg')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBrandblusserGewicht.get_dummy_data()

