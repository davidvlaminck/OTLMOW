# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAantalBoompalen(KeuzelijstField):
    """Hoeveelheid palen waaruit de constructie bestaat."""
    naam = 'KlAantalBoompalen'
    label = 'Aantal boompalen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAantalBoompalen'
    definition = 'Hoeveelheid palen waaruit de constructie bestaat.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAantalBoompalen'
    options = {
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='1',
                              definitie='De constructie bestaat uit 1 boompaal.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAantalBoompalen/1'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='2',
                              definitie='De constructie bestaat uit 2 boompalen.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAantalBoompalen/2'),
        '3': KeuzelijstWaarde(invulwaarde='3',
                              label='3',
                              definitie='De constructie bestaat uit 3 boompalen.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAantalBoompalen/3')
    }

