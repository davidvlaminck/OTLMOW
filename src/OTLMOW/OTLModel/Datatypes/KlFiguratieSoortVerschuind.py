# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFiguratieSoortVerschuind(KeuzelijstField):
    """Soorten van verschuinde figuratie markering."""
    naam = 'KlFiguratieSoortVerschuind'
    label = 'Figuratie soort verschuind'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFiguratieSoortVerschuind'
    definition = 'Soorten van verschuinde figuratie markering.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFiguratieSoortVerschuind'
    options = {
        'letterfiguratiemarkering(schuin)': KeuzelijstWaarde(invulwaarde='letterfiguratiemarkering(schuin)',
                                                             label='letterfiguratiemarkering(schuin)',
                                                             status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                             definitie='Een schuine lettermarking als figuratie zoals BUS, TAXI, TRAM,....',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoortVerschuind/letterfiguratiemarkering(schuin)'),
        'omgekeerde-driehoek(schuin)': KeuzelijstWaarde(invulwaarde='omgekeerde-driehoek(schuin)',
                                                        label='omgekeerde driehoek(schuin)',
                                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                        definitie='Een schuine omgekeerde driehoek markering.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoortVerschuind/omgekeerde-driehoek(schuin)')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlFiguratieSoortVerschuind.get_dummy_data()

