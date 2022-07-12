# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHoogtedetectieModelnaam(KeuzelijstField):
    """Keuzelijst met de gangbare modelnamen van hoogtedetectiesystemen. De modelnamen worden meestal door de leverancier of fabrikant bepaald."""
    naam = 'KlHoogtedetectieModelnaam'
    label = 'Hoogtedetectie modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHoogtedetectieModelnaam'
    definition = 'Keuzelijst met de gangbare modelnamen van hoogtedetectiesystemen. De modelnamen worden meestal door de leverancier of fabrikant bepaald.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHoogtedetectieModelnaam'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlHoogtedetectieModelnaam.get_dummy_data()

