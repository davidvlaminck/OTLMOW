# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPLCModelnaam(KeuzelijstField):
    """De modelnaam van de PLC."""
    naam = 'KlPLCModelnaam'
    label = 'PLC model'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPLCModelnaam'
    definition = 'De modelnaam van de PLC.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPLCModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

