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
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBrandblusserBlusmiddel'
    options = {
        'poeder': KeuzelijstWaarde(invulwaarde='poeder',
                                   label='poeder',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserBlusmiddel/poeder'),
        'schuim': KeuzelijstWaarde(invulwaarde='schuim',
                                   label='schuim',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserBlusmiddel/schuim')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

