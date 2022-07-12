# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVoedingskabelAdersEnSectie(KeuzelijstField):
    """Lijst van mogelijke waarden volgens de catalogusposten van het standaardbestek voor de samenstelling van een voedingskabel volgens het aantal aders en hun dikte in vierkante millimeter."""
    naam = 'KlVoedingskabelAdersEnSectie'
    label = 'Voedingskabel aders en sectie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVoedingskabelAdersEnSectie'
    definition = 'Lijst van mogelijke waarden volgens de catalogusposten van het standaardbestek voor de samenstelling van een voedingskabel volgens het aantal aders en hun dikte in vierkante millimeter.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVoedingskabelAdersEnSectie'
    options = {
        '1-x-1.5-mm2': KeuzelijstWaarde(invulwaarde='1-x-1.5-mm2',
                                        label='1 x 1.5 mm²',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/1-x-1.5-mm2'),
        '1-x-10-mm2': KeuzelijstWaarde(invulwaarde='1-x-10-mm2',
                                       label='1 x 10 mm²',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/1-x-10-mm2'),
        '1-x-16-mm2': KeuzelijstWaarde(invulwaarde='1-x-16-mm2',
                                       label='1 x 16 mm²',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/1-x-16-mm2'),
        '1-x-2.5-mm2': KeuzelijstWaarde(invulwaarde='1-x-2.5-mm2',
                                        label='1 x 2.5 mm²',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/1-x-2.5-mm2'),
        '1-x-25-mm2': KeuzelijstWaarde(invulwaarde='1-x-25-mm2',
                                       label='1 x 25 mm²',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/1-x-25-mm2'),
        '1-x-4-mm2': KeuzelijstWaarde(invulwaarde='1-x-4-mm2',
                                      label='1 x 4 mm²',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/1-x-4-mm2'),
        '1-x-6-mm2': KeuzelijstWaarde(invulwaarde='1-x-6-mm2',
                                      label='1 x 6 mm²',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/1-x-6-mm2'),
        '3-x-10-6-mm2': KeuzelijstWaarde(invulwaarde='3-x-10-6-mm2',
                                         label='3 x 10+6 mm²',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/3-x-10-6-mm2'),
        '3-x-16-10-mm2': KeuzelijstWaarde(invulwaarde='3-x-16-10-mm2',
                                          label='3 x 16+10 mm²',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/3-x-16-10-mm2'),
        '3-x-2.5-mm2': KeuzelijstWaarde(invulwaarde='3-x-2.5-mm2',
                                        label='3 x 2.5 mm²',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/3-x-2.5-mm2'),
        '3-x-25---1-x-16-mm2': KeuzelijstWaarde(invulwaarde='3-x-25---1-x-16-mm2',
                                                label='3 x 25 + 1 x 16 mm²',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/3-x-25---1-x-16-mm2'),
        '3-x-25-16-mm2': KeuzelijstWaarde(invulwaarde='3-x-25-16-mm2',
                                          label='3 x 25+16 mm²',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/3-x-25-16-mm2'),
        '3-x-35-25-mm2': KeuzelijstWaarde(invulwaarde='3-x-35-25-mm2',
                                          label='3 x 35+25 mm²',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/3-x-35-25-mm2'),
        '3g2.5-mm2': KeuzelijstWaarde(invulwaarde='3g2.5-mm2',
                                      label='3G2.5 mm²',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/3g2.5-mm2'),
        '4-x-1.5-mm2': KeuzelijstWaarde(invulwaarde='4-x-1.5-mm2',
                                        label='4 x 1.5 mm²',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/4-x-1.5-mm2'),
        '4-x-10-mm2': KeuzelijstWaarde(invulwaarde='4-x-10-mm2',
                                       label='4 x 10 mm²',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/4-x-10-mm2'),
        '4-x-150-mm2': KeuzelijstWaarde(invulwaarde='4-x-150-mm2',
                                        label='4 x 150 mm²',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/4-x-150-mm2'),
        '4-x-16-mm2': KeuzelijstWaarde(invulwaarde='4-x-16-mm2',
                                       label='4 x 16 mm²',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/4-x-16-mm2'),
        '4-x-2.5-mm2': KeuzelijstWaarde(invulwaarde='4-x-2.5-mm2',
                                        label='4 x 2.5 mm²',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/4-x-2.5-mm2'),
        '4-x-25-mm2': KeuzelijstWaarde(invulwaarde='4-x-25-mm2',
                                       label='4 x 25 mm²',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/4-x-25-mm2'),
        '4-x-35-mm2': KeuzelijstWaarde(invulwaarde='4-x-35-mm2',
                                       label='4 x 35 mm²',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/4-x-35-mm2'),
        '4-x-4-mm2': KeuzelijstWaarde(invulwaarde='4-x-4-mm2',
                                      label='4 x 4 mm²',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/4-x-4-mm2'),
        '4-x-50-mm2': KeuzelijstWaarde(invulwaarde='4-x-50-mm2',
                                       label='4 x 50 mm²',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/4-x-50-mm2'),
        '4-x-6-mm2': KeuzelijstWaarde(invulwaarde='4-x-6-mm2',
                                      label='4 x 6 mm²',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/4-x-6-mm2'),
        '4-x-95-mm2': KeuzelijstWaarde(invulwaarde='4-x-95-mm2',
                                       label='4 x 95 mm²',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/4-x-95-mm2'),
        '5-x-10-mm2': KeuzelijstWaarde(invulwaarde='5-x-10-mm2',
                                       label='5 x 10 mm²',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/5-x-10-mm2'),
        '5-x-2.5-mm2': KeuzelijstWaarde(invulwaarde='5-x-2.5-mm2',
                                        label='5 x 2.5 mm²',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/5-x-2.5-mm2'),
        'zonder-bijkomende-specificatie': KeuzelijstWaarde(invulwaarde='zonder-bijkomende-specificatie',
                                                           label='zonder bijkomende specificatie',
                                                           status='ingebruik',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelAdersEnSectie/zonder-bijkomende-specificatie')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlVoedingskabelAdersEnSectie.get_dummy_data()

