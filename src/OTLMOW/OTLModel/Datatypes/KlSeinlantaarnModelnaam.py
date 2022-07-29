# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSeinlantaarnModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor Seinlantaarn."""
    naam = 'KlSeinlantaarnModelnaam'
    label = 'seinlantaarn modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlSeinlantaarnModelnaam'
    definition = 'Keuzelijst met modelnamen voor Seinlantaarn.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSeinlantaarnModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

