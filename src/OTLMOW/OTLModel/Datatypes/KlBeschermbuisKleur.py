# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeschermbuisKleur(KeuzelijstField):
    """TODO"""
    naam = 'KlBeschermbuisKleur'
    label = 'Beschermbuiskleur'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBeschermbuisKleur'
    definition = 'TODO'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeschermbuisKleur'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

