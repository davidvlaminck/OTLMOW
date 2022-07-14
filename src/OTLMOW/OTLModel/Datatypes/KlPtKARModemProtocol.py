# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPtKARModemProtocol(KeuzelijstField):
    """Beschrijft het protocol dat de PT-KAR-Modem gebruikt om te communiceren."""
    naam = 'KlPtKARModemProtocol'
    label = 'PT-KAR-modem protocol'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPtKARModemProtocol'
    definition = 'Beschrijft het protocol dat de PT-KAR-Modem gebruikt om te communiceren.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPtKARModemProtocol'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

