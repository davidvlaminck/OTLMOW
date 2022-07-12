# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIpPowerSwitchType(KeuzelijstField):
    """Type van de IP powerswitch."""
    naam = 'KlIpPowerSwitchType'
    label = 'IP powerswitch type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIpPowerSwitchType'
    definition = 'Type van de IP powerswitch.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIpPowerSwitchType'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlIpPowerSwitchType.get_dummy_data()

