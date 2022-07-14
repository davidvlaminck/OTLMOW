# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFietstelsysteemMerk(KeuzelijstField):
    """Lijst van mogelijke merknamen voor fietstelsystemen."""
    naam = 'KlFietstelsysteemMerk'
    label = 'Merknaam fietstelsysteem'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFietstelsysteemMerk'
    definition = 'Lijst van mogelijke merknamen voor fietstelsystemen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFietstelsysteemMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

