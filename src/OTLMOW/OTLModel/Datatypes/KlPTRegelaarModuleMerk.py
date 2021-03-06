# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPTRegelaarModuleMerk(KeuzelijstField):
    """Keuzelijst met merknamen voor PTRegelaarModule."""
    naam = 'KlPTRegelaarModuleMerk'
    label = 'PT regelaarmodule merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlPTRegelaarModuleMerk'
    definition = 'Keuzelijst met merknamen voor PTRegelaarModule.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPTRegelaarModuleMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

