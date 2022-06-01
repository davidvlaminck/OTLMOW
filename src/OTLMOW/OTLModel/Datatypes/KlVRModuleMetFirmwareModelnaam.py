# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVRModuleMetFirmwareModelnaam(KeuzelijstField):
    """Lijst met modelnamen voor VR-modules met firmware."""
    naam = 'KlVRModuleMetFirmwareModelnaam'
    label = 'VR-module met firmware modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVRModuleMetFirmwareModelnaam'
    definition = 'Lijst met modelnamen voor VR-modules met firmware.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVRModuleMetFirmwareModelnaam'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlVRModuleMetFirmwareModelnaam.get_dummy_data()

