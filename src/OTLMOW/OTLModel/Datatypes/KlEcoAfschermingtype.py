# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEcoAfschermingtype(KeuzelijstField):
    """Types van afscherming."""
    naam = 'KlEcoAfschermingtype'
    label = 'Afschermingtype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEcoAfschermingtype'
    definition = 'Types van afscherming.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEcoAfschermingtype'
    options = {
        'heidematten': KeuzelijstWaarde(invulwaarde='heidematten',
                                        label='heidematten',
                                        definitie='Een afscherming bestaande uit heidematten.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoAfschermingtype/heidematten'),
        'houten': KeuzelijstWaarde(invulwaarde='houten',
                                   label='houten',
                                   definitie='Een afscherming bestaande uit houten schermen.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoAfschermingtype/houten'),
        'metalen': KeuzelijstWaarde(invulwaarde='metalen',
                                    label='metalen',
                                    definitie='Een afscherming bestaande uit metalen schermen.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoAfschermingtype/metalen')
    }

