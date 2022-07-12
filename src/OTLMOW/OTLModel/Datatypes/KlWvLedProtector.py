# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLedProtector(KeuzelijstField):
    """Type doorschijnende kap ter bescherming van de LED's (vlak glas, polycarbonaat,...)."""
    naam = 'KlWvLedProtector'
    label = 'WV protector'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedProtector'
    definition = "Type doorschijnende kap ter bescherming van de LED's (vlak glas, polycarbonaat,...)."
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedProtector'
    options = {
        'gebogen-glas': KeuzelijstWaarde(invulwaarde='gebogen-glas',
                                         label='gebogen glas',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedProtector/gebogen-glas'),
        'polycarbonaat': KeuzelijstWaarde(invulwaarde='polycarbonaat',
                                          label='polycarbonaat',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedProtector/polycarbonaat'),
        'vlak-glas': KeuzelijstWaarde(invulwaarde='vlak-glas',
                                      label='vlak glas',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedProtector/vlak-glas')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlWvLedProtector.get_dummy_data()

