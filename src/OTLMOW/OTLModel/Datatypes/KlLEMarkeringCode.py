# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEMarkeringCode(KeuzelijstField):
    """Codes van de markering op lijnvormige elementen."""
    naam = 'KlLEMarkeringCode'
    label = 'Markering code'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEMarkeringCode'
    definition = 'Codes van de markering op lijnvormige elementen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEMarkeringCode'
    options = {
        'DIV-BIG': KeuzelijstWaarde(invulwaarde='DIV-BIG',
                                    label='DIV-BIG',
                                    definitie='De code voor LE markering biggenrug',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringCode/DIV-BIG'),
        'DIV-BRDSTN': KeuzelijstWaarde(invulwaarde='DIV-BRDSTN',
                                       label='DIV-BRDSTN',
                                       definitie='De code voor LE markering boordsteen',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringCode/DIV-BRDSTN'),
        'DIV-BRDSTN-PV': KeuzelijstWaarde(invulwaarde='DIV-BRDSTN-PV',
                                          label='DIV-BRDSTN-PV',
                                          definitie='De code voor LE markering boordsteen parkeerverbod',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringCode/DIV-BRDSTN-PV'),
        'DIV-NJ': KeuzelijstWaarde(invulwaarde='DIV-NJ',
                                   label='DIV-NJ',
                                   definitie='De code voor LE markering New Jersey',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringCode/DIV-NJ')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlLEMarkeringCode.get_dummy_data()

