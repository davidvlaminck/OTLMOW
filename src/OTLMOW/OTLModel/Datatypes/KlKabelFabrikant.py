# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKabelFabrikant(KeuzelijstField):
    """Lijst met producenten van kabels."""
    naam = 'KlKabelFabrikant'
    label = 'Kabel fabrikant'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlKabelFabrikant'
    definition = 'Lijst met producenten van kabels.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKabelFabrikant'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

