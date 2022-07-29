# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPTRegelaarModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor PTRegelaar."""
    naam = 'KlPTRegelaarModelnaam'
    label = 'PT regelaar modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPTRegelaarModelnaam'
    definition = 'Keuzelijst met modelnamen voor PTRegelaar.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPTRegelaarModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

