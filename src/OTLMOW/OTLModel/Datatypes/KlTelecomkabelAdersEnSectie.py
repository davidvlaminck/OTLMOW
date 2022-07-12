# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTelecomkabelAdersEnSectie(KeuzelijstField):
    """Lijst van mogelijke waarden volgens de catalogusposten van het standaardbestek voor de samenstelling van een telecomkabel volgens het aantal aders en hun dikte in vierkante millimeter."""
    naam = 'KlTelecomkabelAdersEnSectie'
    label = 'Telecomkabel aders en sectie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTelecomkabelAdersEnSectie'
    definition = 'Lijst van mogelijke waarden volgens de catalogusposten van het standaardbestek voor de samenstelling van een telecomkabel volgens het aantal aders en hun dikte in vierkante millimeter.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTelecomkabelAdersEnSectie'
    options = {
        '100-x-2-x-1-mm2': KeuzelijstWaarde(invulwaarde='100-x-2-x-1-mm2',
                                            label='100 x 2 X 1 mm²',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelAdersEnSectie/100-x-2-x-1-mm2'),
        '10x4x1': KeuzelijstWaarde(invulwaarde='10x4x1',
                                   label='10x4x1',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelAdersEnSectie/10x4x1'),
        '20-x-2-x-1-mm2': KeuzelijstWaarde(invulwaarde='20-x-2-x-1-mm2',
                                           label='20 x 2 X 1 mm²',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelAdersEnSectie/20-x-2-x-1-mm2'),
        '20x4x1': KeuzelijstWaarde(invulwaarde='20x4x1',
                                   label='20x4x1',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelAdersEnSectie/20x4x1'),
        '21-x-2-x-1-mm2': KeuzelijstWaarde(invulwaarde='21-x-2-x-1-mm2',
                                           label='21 x 2 X 1 mm²',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelAdersEnSectie/21-x-2-x-1-mm2'),
        '30x4x1': KeuzelijstWaarde(invulwaarde='30x4x1',
                                   label='30x4x1',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelAdersEnSectie/30x4x1'),
        '40x4x1': KeuzelijstWaarde(invulwaarde='40x4x1',
                                   label='40x4x1',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelAdersEnSectie/40x4x1'),
        '48-vezels': KeuzelijstWaarde(invulwaarde='48-vezels',
                                      label='48 vezels',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelAdersEnSectie/48-vezels'),
        '5x4x1': KeuzelijstWaarde(invulwaarde='5x4x1',
                                  label='5x4x1',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelAdersEnSectie/5x4x1'),
        '96-vezels': KeuzelijstWaarde(invulwaarde='96-vezels',
                                      label='96 vezels',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelAdersEnSectie/96-vezels'),
        'zonder-verdere-specificatie': KeuzelijstWaarde(invulwaarde='zonder-verdere-specificatie',
                                                        label='zonder verdere specificatie',
                                                        status='ingebruik',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelAdersEnSectie/zonder-verdere-specificatie')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlTelecomkabelAdersEnSectie.get_dummy_data()

