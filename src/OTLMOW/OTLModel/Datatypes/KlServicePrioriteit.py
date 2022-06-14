# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlServicePrioriteit(KeuzelijstField):
    """Het prioriteitsniveau dat aangeeft hoe dringend iets moet onderhouden/gerepareerd worden"""
    naam = 'KlServicePrioriteit'
    label = 'Serviceprioriteit'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlServicePrioriteit'
    definition = 'Het prioriteitsniveau dat aangeeft hoe dringend iets moet onderhouden/gerepareerd worden'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlServicePrioriteit'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlServicePrioriteit.get_dummy_data()

