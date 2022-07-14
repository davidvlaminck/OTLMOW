# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDeurFabrikant(KeuzelijstField):
    """Lijst van fabrikanten van deuren."""
    naam = 'KlDeurFabrikant'
    label = 'Deur fabrikant'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlDeurFabrikant'
    definition = 'Lijst van fabrikanten van deuren.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDeurFabrikant'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

