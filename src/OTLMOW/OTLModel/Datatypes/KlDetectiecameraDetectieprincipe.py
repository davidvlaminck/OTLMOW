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
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDetectiecameraDetectieprincipe'
    options = {
        'optisch': KeuzelijstWaarde(invulwaarde='optisch',
                                    label='optisch',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectiecameraDetectieprincipe/optisch'),
        'thermografisch': KeuzelijstWaarde(invulwaarde='thermografisch',
                                           label='thermografisch',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectiecameraDetectieprincipe/thermografisch')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

