# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLETrottoirbandVorm(KeuzelijstField):
    """De vormen van een trottoirband."""
    naam = 'KlLETrottoirbandVorm'
    label = 'Trottoirband vorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLETrottoirbandVorm'
    definition = 'De vormen van een trottoirband.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLETrottoirbandVorm'
    options = {
        'afgeschuind': KeuzelijstWaarde(invulwaarde='afgeschuind',
                                        label='afgeschuind',
                                        status='ingebruik',
                                        definitie='Afgeschuind',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandVorm/afgeschuind')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

