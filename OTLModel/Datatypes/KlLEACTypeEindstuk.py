# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACTypeEindstuk(KeuzelijstField):
    """De verschillende types eindstukken."""
    naam = 'KlLEACTypeEindstuk'
    label = 'Type eindstuk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACTypeEindstuk'
    definition = 'De verschillende types eindstukken.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACTypeEindstuk'
    options = {
        'naar-beneden-afgebogen': KeuzelijstWaarde(invulwaarde='naar-beneden-afgebogen',
                                                   label='naar beneden afgebogen',
                                                   definitie='naar beneden afgebogen',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACTypeEindstuk/naar-beneden-afgebogen'),
        'schelp': KeuzelijstWaarde(invulwaarde='schelp',
                                   label='schelp',
                                   definitie='schelp',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACTypeEindstuk/schelp'),
        'uitgebogen': KeuzelijstWaarde(invulwaarde='uitgebogen',
                                       label='uitgebogen',
                                       definitie='uitgebogen',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACTypeEindstuk/uitgebogen')
    }

