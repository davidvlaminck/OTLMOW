# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFietstelsysteemModelnaam(KeuzelijstField):
    """Lijst met mogelijke modelnamen voor fietstelsystemen."""
    naam = 'KlFietstelsysteemModelnaam'
    label = 'Modelnaam fietstelsysteem'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFietstelsysteemModelnaam'
    definition = 'Lijst met mogelijke modelnamen voor fietstelsystemen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFietstelsysteemModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

