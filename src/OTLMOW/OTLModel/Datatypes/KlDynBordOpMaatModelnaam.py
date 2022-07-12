# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordOpMaatModelnaam(KeuzelijstField):
    """Keuzelijst met de gangbare modelnamen van dynamische borden op maat. De modelnamen worden meestal door de leverancier of fabrikant bepaald."""
    naam = 'KlDynBordOpMaatModelnaam'
    label = 'Keuzelijst modelnamen voor dynamische borden op maat'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordOpMaatModelnaam'
    definition = 'Keuzelijst met de gangbare modelnamen van dynamische borden op maat. De modelnamen worden meestal door de leverancier of fabrikant bepaald.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordOpMaatModelnaam'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlDynBordOpMaatModelnaam.get_dummy_data()

