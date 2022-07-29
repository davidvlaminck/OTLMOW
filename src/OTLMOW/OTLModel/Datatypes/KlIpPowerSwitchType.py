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
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

