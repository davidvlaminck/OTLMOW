# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZenderModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor Zender."""
    naam = 'KlZenderModelnaam'
    label = 'zender modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlZenderModelnaam'
    definition = 'Keuzelijst met modelnamen voor Zender.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZenderModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

