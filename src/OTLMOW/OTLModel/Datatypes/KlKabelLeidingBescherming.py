# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKabelLeidingBescherming(KeuzelijstField):
    """Lijst met mogelijke types bijkomende mechanische bescherming van kabels of leidingen."""
    naam = 'KlKabelLeidingBescherming'
    label = 'Kabels en Leidingen bescherming'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKabelLeidingBescherming'
    definition = 'Lijst met mogelijke types bijkomende mechanische bescherming van kabels of leidingen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKabelLeidingBescherming'
    options = {
        'kabeldekband': KeuzelijstWaarde(invulwaarde='kabeldekband',
                                         label='kabeldekband',
                                         status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/kabeldekband'),
        'mager-beton': KeuzelijstWaarde(invulwaarde='mager-beton',
                                        label='mager beton',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/mager-beton'),
        'niet-gekend': KeuzelijstWaarde(invulwaarde='niet-gekend',
                                        label='niet gekend',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/niet-gekend'),
        'omegaprofiel': KeuzelijstWaarde(invulwaarde='omegaprofiel',
                                         label='omegaprofiel',
                                         status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/omegaprofiel'),
        'synthetische-kabeldekking': KeuzelijstWaarde(invulwaarde='synthetische-kabeldekking',
                                                      label='synthetische kabeldekking',
                                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/synthetische-kabeldekking'),
        'tegels': KeuzelijstWaarde(invulwaarde='tegels',
                                   label='tegels',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/tegels'),
        'u-ijzers': KeuzelijstWaarde(invulwaarde='u-ijzers',
                                     label='u-ijzers',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/u-ijzers'),
        'waarschuwingslint': KeuzelijstWaarde(invulwaarde='waarschuwingslint',
                                              label='waarschuwingslint',
                                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/waarschuwingslint'),
        'waarschuwingsnet': KeuzelijstWaarde(invulwaarde='waarschuwingsnet',
                                             label='waarschuwingsnet',
                                             status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/waarschuwingsnet')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlKabelLeidingBescherming.get_dummy_data()

