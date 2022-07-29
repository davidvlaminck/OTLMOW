# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWeggebondendetectorMerk(KeuzelijstField):
    """Keuzelijst met merknamen voor Weggebondendetector."""
    naam = 'KlWeggebondendetectorMerk'
    label = 'Weggebondendetector merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeggebondendetectorMerk'
    definition = 'Keuzelijst met merknamen voor Weggebondendetector.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeggebondendetectorMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

