# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVrComKaartTypeOpslaggeheugen(KeuzelijstField):
    """Keuzelijst met verschillende types geheugen van een VRCommunicatiekaart."""
    naam = 'KlVrComKaartTypeOpslaggeheugen'
    label = 'VR-communicatiekaart type opslaggeheugen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVrComKaartTypeOpslaggeheugen'
    definition = 'Keuzelijst met verschillende types geheugen van een VRCommunicatiekaart.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVrComKaartTypeOpslaggeheugen'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

