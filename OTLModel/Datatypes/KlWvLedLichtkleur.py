# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLedLichtkleur(KeuzelijstField):
    """Beschrijving van de kleur van het licht adhv de naam van de kleur."""
    naam = 'KlWvLedLichtkleur'
    label = 'WV LED lichtkleur'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedLichtkleur'
    definition = 'Beschrijving van de kleur van het licht adhv de naam van de kleur.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedLichtkleur'
    options = {
        'amber': KeuzelijstWaarde(invulwaarde='amber',
                                  label='amber',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtkleur/amber'),
        'blauw': KeuzelijstWaarde(invulwaarde='blauw',
                                  label='blauw',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtkleur/blauw'),
        'rood': KeuzelijstWaarde(invulwaarde='rood',
                                 label='rood',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtkleur/rood'),
        'wit': KeuzelijstWaarde(invulwaarde='wit',
                                label='wit',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtkleur/wit')
    }

