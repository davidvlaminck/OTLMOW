# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBuitenkastVerfraaid(KeuzelijstField):
    """Mogelijke types voor verfraaiing als combinatie van aan- en afwezigheid en al dan niet vegund."""
    naam = 'KlBuitenkastVerfraaid'
    label = 'Verfraaiing buitenkast'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlBuitenkastVerfraaid'
    definition = 'Mogelijke types voor verfraaiing als combinatie van aan- en afwezigheid en al dan niet vegund.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBuitenkastVerfraaid'
    options = {
        'ja': KeuzelijstWaarde(invulwaarde='ja',
                               label='ja',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBuitenkastVerfraaid/ja'),
        'ja-niet-vergund': KeuzelijstWaarde(invulwaarde='ja-niet-vergund',
                                            label='ja niet vergund',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBuitenkastVerfraaid/ja-niet-vergund'),
        'nee': KeuzelijstWaarde(invulwaarde='nee',
                                label='nee',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBuitenkastVerfraaid/nee')
    }

