# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCSchermtype(KeuzelijstField):
    """De mogelijke schermtypes (vlak, niet-vlak)."""
    naam = 'KlLEGCSchermtype'
    label = 'Schermtype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCSchermtype'
    definition = 'De mogelijke schermtypes (vlak, niet-vlak).'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCSchermtype'
    options = {
        'niet-vlak': KeuzelijstWaarde(invulwaarde='niet-vlak',
                                      label='niet-vlak',
                                      definitie='De niet-vlakke schermen zijn de schermen die niet kunnen getest worden volgens de normen NBN EN 1793-1 NBN EN 1793-2.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCSchermtype/niet-vlak'),
        'vlak': KeuzelijstWaarde(invulwaarde='vlak',
                                 label='vlak',
                                 definitie='De vlakke schermen zijn de schermen die kunnen getest worden volgens de normen NBN EN 1793-1 NBN EN 1793-2.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCSchermtype/vlak')
    }

