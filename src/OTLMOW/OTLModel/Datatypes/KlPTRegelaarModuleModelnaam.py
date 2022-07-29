# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPTRegelaarModuleModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor PTRegelaarModule."""
    naam = 'KlPTRegelaarModuleModelnaam'
    label = 'PT regelaarmodule modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlPTRegelaarModuleModelnaam'
    definition = 'Keuzelijst met modelnamen voor PTRegelaarModule.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPTRegelaarModuleModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

