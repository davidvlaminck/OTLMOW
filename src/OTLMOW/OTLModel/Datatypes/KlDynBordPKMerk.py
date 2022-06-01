# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordPKMerk(KeuzelijstField):
    """Keuzelijst met de gangbare merken van Pijl-Kruisborden. De merken verwijzen doorgaans naar de fabrikant of leverancier."""
    naam = 'KlDynBordPKMerk'
    label = 'Dyn bord PK merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordPKMerk'
    definition = 'Keuzelijst met de gangbare merken van Pijl-Kruisborden. De merken verwijzen doorgaans naar de fabrikant of leverancier.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordPKMerk'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlDynBordPKMerk.get_dummy_data()

