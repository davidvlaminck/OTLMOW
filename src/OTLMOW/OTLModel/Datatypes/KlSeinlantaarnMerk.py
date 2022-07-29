# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSeinlantaarnMerk(KeuzelijstField):
    """Keuzelijst met merknamen voor Seinlantaarn."""
    naam = 'KlSeinlantaarnMerk'
    label = 'seinlantaarn merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlSeinlantaarnMerk'
    definition = 'Keuzelijst met merknamen voor Seinlantaarn.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSeinlantaarnMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

