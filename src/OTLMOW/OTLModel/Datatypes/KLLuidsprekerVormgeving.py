# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KLLuidsprekerVormgeving(KeuzelijstField):
    """Types luidspreker volgens hun vormfactor."""
    naam = 'KLLuidsprekerVormgeving'
    label = 'Luidspreker vormgeving'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KLLuidsprekerVormgeving'
    definition = 'Types luidspreker volgens hun vormfactor.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KLLuidsprekerVormgeving'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

