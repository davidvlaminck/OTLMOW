# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHardwareCdDvdTape(KeuzelijstField):
    """CD, DVD, Tape."""
    naam = 'KlHardwareCdDvdTape'
    label = 'Hardware CD DVD tape'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlHardwareCdDvdTape'
    definition = 'CD, DVD, Tape.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHardwareCdDvdTape'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

