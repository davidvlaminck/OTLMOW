# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeerslichtModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor Verkeerslicht."""
    naam = 'KlVerkeerslichtModelnaam'
    label = 'verkeerslicht modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerkeerslichtModelnaam'
    definition = 'Keuzelijst met modelnamen voor Verkeerslicht.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeerslichtModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

