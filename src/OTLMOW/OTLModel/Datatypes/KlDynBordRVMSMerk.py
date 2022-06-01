# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordRVMSMerk(KeuzelijstField):
    """Keuzelijst met de gangbare merken van RVMS borden. De merken verwijzen doorgaans naar de fabrikant of leverancier."""
    naam = 'KlDynBordRVMSMerk'
    label = 'Dyn bord RVMS merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordRVMSMerk'
    definition = 'Keuzelijst met de gangbare merken van RVMS borden. De merken verwijzen doorgaans naar de fabrikant of leverancier.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordRVMSMerk'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlDynBordRVMSMerk.get_dummy_data()

