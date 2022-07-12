# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBestratingSteenverband(KeuzelijstField):
    """De steenverbanden van de bestrating."""
    naam = 'KlBestratingSteenverband'
    label = 'Bestrating steenverband'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBestratingSteenverband'
    definition = 'De steenverbanden van de bestrating.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBestratingSteenverband'
    options = {
        'blokverband': KeuzelijstWaarde(invulwaarde='blokverband',
                                        label='blokverband',
                                        status='ingebruik',
                                        definitie='Blokverband',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/blokverband'),
        'elleboogverband': KeuzelijstWaarde(invulwaarde='elleboogverband',
                                            label='elleboogverband',
                                            status='ingebruik',
                                            definitie='Elleboogverband',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/elleboogverband'),
        'halfsteensverband': KeuzelijstWaarde(invulwaarde='halfsteensverband',
                                              label='halfsteensverband',
                                              status='ingebruik',
                                              definitie='Halfsteensverband',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/halfsteensverband'),
        'keperverband': KeuzelijstWaarde(invulwaarde='keperverband',
                                         label='keperverband',
                                         status='ingebruik',
                                         definitie='Keperverband',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/keperverband'),
        'schelpen--of-pauwstaartverband': KeuzelijstWaarde(invulwaarde='schelpen--of-pauwstaartverband',
                                                           label='schelpen- of pauwstaartverband',
                                                           status='ingebruik',
                                                           definitie='Schelpen- of pauwstaartverband',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/schelpen--of-pauwstaartverband'),
        'schubbenverband': KeuzelijstWaarde(invulwaarde='schubbenverband',
                                            label='schubbenverband',
                                            status='ingebruik',
                                            definitie='Schubbenverband',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/schubbenverband'),
        'segmentverband': KeuzelijstWaarde(invulwaarde='segmentverband',
                                           label='segmentverband',
                                           status='ingebruik',
                                           definitie='Segmentverband',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/segmentverband'),
        'visgraatverband': KeuzelijstWaarde(invulwaarde='visgraatverband',
                                            label='visgraatverband',
                                            status='ingebruik',
                                            definitie='Visgraatverband',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/visgraatverband'),
        'waaierverband': KeuzelijstWaarde(invulwaarde='waaierverband',
                                          label='waaierverband',
                                          status='ingebruik',
                                          definitie='Waaierverband',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingSteenverband/waaierverband')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBestratingSteenverband.get_dummy_data()

