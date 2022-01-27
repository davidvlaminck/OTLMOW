# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBestratingSteenverband(KeuzelijstField):
    """De steenverbanden van de bestrating."""
    naam = 'KlBestratingSteenverband'
    label = 'Bestrating steenverband'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBestratingSteenverband'
    definition = 'De steenverbanden van de bestrating.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBestratingSteenverband'
    options = {
        'blokverband': KeuzelijstWaarde(invulwaarde='blokverband',
                                        label='blokverband',
                                        definitie='Blokverband',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/blokverband'),
        'elleboogverband': KeuzelijstWaarde(invulwaarde='elleboogverband',
                                            label='elleboogverband',
                                            definitie='Elleboogverband',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/elleboogverband'),
        'halfsteensverband': KeuzelijstWaarde(invulwaarde='halfsteensverband',
                                              label='halfsteensverband',
                                              definitie='Halfsteensverband',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/halfsteensverband'),
        'keperverband': KeuzelijstWaarde(invulwaarde='keperverband',
                                         label='keperverband',
                                         definitie='Keperverband',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/keperverband'),
        'schelpen--of-pauwstaartverband': KeuzelijstWaarde(invulwaarde='schelpen--of-pauwstaartverband',
                                                           label='schelpen- of pauwstaartverband',
                                                           definitie='Schelpen- of pauwstaartverband',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/schelpen--of-pauwstaartverband'),
        'schubbenverband': KeuzelijstWaarde(invulwaarde='schubbenverband',
                                            label='schubbenverband',
                                            definitie='Schubbenverband',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/schubbenverband'),
        'segmentverband': KeuzelijstWaarde(invulwaarde='segmentverband',
                                           label='segmentverband',
                                           definitie='Segmentverband',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/segmentverband'),
        'visgraatverband': KeuzelijstWaarde(invulwaarde='visgraatverband',
                                            label='visgraatverband',
                                            definitie='Visgraatverband',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/visgraatverband'),
        'waaierverband': KeuzelijstWaarde(invulwaarde='waaierverband',
                                          label='waaierverband',
                                          definitie='Waaierverband',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/waaierverband')
    }

