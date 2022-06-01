# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDetectiecameraDetectieprincipe(KeuzelijstField):
    """Keuzelijst met detectieprincipes voor Detectiecamera."""
    naam = 'KlDetectiecameraDetectieprincipe'
    label = 'Detectiecamera detectieprincipe'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDetectiecameraDetectieprincipe'
    definition = 'Keuzelijst met detectieprincipes voor Detectiecamera.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDetectiecameraDetectieprincipe'
    options = {
        'optisch': KeuzelijstWaarde(invulwaarde='optisch',
                                    label='optisch',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectiecameraDetectieprincipe/optisch'),
        'thermografisch': KeuzelijstWaarde(invulwaarde='thermografisch',
                                           label='thermografisch',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectiecameraDetectieprincipe/thermografisch')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlDetectiecameraDetectieprincipe.get_dummy_data()

