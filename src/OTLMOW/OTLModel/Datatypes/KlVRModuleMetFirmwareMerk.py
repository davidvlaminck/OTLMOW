# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVRModuleMetFirmwareMerk(KeuzelijstField):
    """Lijst met merken van VR-modules met firmware."""
    naam = 'KlVRModuleMetFirmwareMerk'
    label = 'VR-module met firmware merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVRModuleMetFirmwareMerk'
    definition = 'Lijst met merken van VR-modules met firmware.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVRModuleMetFirmwareMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

