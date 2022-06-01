# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRetroreflecterendVerkeersbordMerk(KeuzelijstField):
    """Keuzelijst met merknamen van retroreflecterende verkeersborden. De merknaam duidt op de leverancier of producent van het verkeersbord."""
    naam = 'KlRetroreflecterendVerkeersbordMerk'
    label = 'Retroreflecterend Verkeersbord Merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRetroreflecterendVerkeersbordMerk'
    definition = 'Keuzelijst met merknamen van retroreflecterende verkeersborden. De merknaam duidt op de leverancier of producent van het verkeersbord.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRetroreflecterendVerkeersbordMerk'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlRetroreflecterendVerkeersbordMerk.get_dummy_data()

