# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCADOMerk(KeuzelijstField):
    """Het merk van de calamiteitendoorsteek."""
    naam = 'KlCADOMerk'
    label = 'Calamiteitendoorsteek merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCADOMerk'
    definition = 'Het merk van de calamiteitendoorsteek.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCADOMerk'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlCADOMerk.get_dummy_data()

