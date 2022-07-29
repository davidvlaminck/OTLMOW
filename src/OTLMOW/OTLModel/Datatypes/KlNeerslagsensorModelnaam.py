# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNeerslagsensorModelnaam(KeuzelijstField):
    """De modelnaam van de neerslagsensor."""
    naam = 'KlNeerslagsensorModelnaam'
    label = 'Neerslagsensor modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNeerslagsensorModelnaam'
    definition = 'De modelnaam van de neerslagsensor.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNeerslagsensorModelnaam'
    options = {
        'WS100': KeuzelijstWaarde(invulwaarde='WS100',
                                  label='WS100',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNeerslagsensorModelnaam/WS100')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

