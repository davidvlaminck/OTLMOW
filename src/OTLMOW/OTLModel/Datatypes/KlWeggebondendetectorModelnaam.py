# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWeggebondendetectorModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor Weggebondendetector."""
    naam = 'KlWeggebondendetectorModelnaam'
    label = 'Weggebondendetector modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeggebondendetectorModelnaam'
    definition = 'Keuzelijst met modelnamen voor Weggebondendetector.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeggebondendetectorModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

