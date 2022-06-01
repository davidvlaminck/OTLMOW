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
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KLLuidsprekerVormgeving'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KLLuidsprekerVormgeving.get_dummy_data()

