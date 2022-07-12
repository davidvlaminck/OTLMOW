# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGPUMerk(KeuzelijstField):
    """Het merk van de GPU."""
    naam = 'KlGPUMerk'
    label = 'GPU merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGPUMerk'
    definition = 'Het merk van de GPU.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGPUMerk'
    options = {
        'nvidia': KeuzelijstWaarde(invulwaarde='nvidia',
                                   label='Nvidia',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Nvidia',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGPUMerk/nvidia')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlGPUMerk.get_dummy_data()

