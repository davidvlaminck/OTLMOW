# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHoogtedetectieMerk(KeuzelijstField):
    """Keuzelijst met de gangbare merken van hoogtedetectiesystemen. De merken verwijzen doorgaans naar de fabrikant of leverancier."""
    naam = 'KlHoogtedetectieMerk'
    label = 'Hoogtedetectie merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHoogtedetectieMerk'
    definition = 'Keuzelijst met de gangbare merken van hoogtedetectiesystemen. De merken verwijzen doorgaans naar de fabrikant of leverancier.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHoogtedetectieMerk'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlHoogtedetectieMerk.get_dummy_data()

