# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEcoAfschermingtype(KeuzelijstField):
    """Types van afscherming."""
    naam = 'KlEcoAfschermingtype'
    label = 'Afschermingtype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEcoAfschermingtype'
    definition = 'Types van afscherming.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEcoAfschermingtype'
    options = {
        'heidematten': KeuzelijstWaarde(invulwaarde='heidematten',
                                        label='heidematten',
                                        status='ingebruik',
                                        definitie='Een afscherming bestaande uit heidematten.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoAfschermingtype/heidematten'),
        'houten': KeuzelijstWaarde(invulwaarde='houten',
                                   label='houten',
                                   status='ingebruik',
                                   definitie='Een afscherming bestaande uit houten schermen.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoAfschermingtype/houten'),
        'metalen': KeuzelijstWaarde(invulwaarde='metalen',
                                    label='metalen',
                                    status='ingebruik',
                                    definitie='Een afscherming bestaande uit metalen schermen.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoAfschermingtype/metalen')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

