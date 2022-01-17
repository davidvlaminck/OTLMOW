# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


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
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserBlusmiddel/poeder'),
        'schuim': KeuzelijstWaarde(invulwaarde='schuim',
                                   label='schuim',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserBlusmiddel/schuim')
    }

