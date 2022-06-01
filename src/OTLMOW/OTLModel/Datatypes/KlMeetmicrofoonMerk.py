# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMeetmicrofoonMerk(KeuzelijstField):
    """Het merk van de meetmicrofoon."""
    naam = 'KlMeetmicrofoonMerk'
    label = 'Meetmicrofoon merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMeetmicrofoonMerk'
    definition = 'Het merk van de meetmicrofoon.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMeetmicrofoonMerk'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlMeetmicrofoonMerk.get_dummy_data()

