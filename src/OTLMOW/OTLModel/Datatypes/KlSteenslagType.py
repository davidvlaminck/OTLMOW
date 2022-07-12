# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSteenslagType(KeuzelijstField):
    """Steenslag types."""
    naam = 'KlSteenslagType'
    label = 'Steenslag type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSteenslagType'
    definition = 'Steenslag types.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSteenslagType'
    options = {
        'type-IA': KeuzelijstWaarde(invulwaarde='type-IA',
                                    label='type IA',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='type IA',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IA'),
        'type-IB': KeuzelijstWaarde(invulwaarde='type-IB',
                                    label='type IB',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='type IB',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IB'),
        'type-IIA': KeuzelijstWaarde(invulwaarde='type-IIA',
                                     label='type IIA',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='type IIA',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IIA'),
        'type-IIB': KeuzelijstWaarde(invulwaarde='type-IIB',
                                     label='type IIB',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='type IIB',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IIB'),
        'type-IIIA': KeuzelijstWaarde(invulwaarde='type-IIIA',
                                      label='type IIIA',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='type IIIA',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IIIA'),
        'type-IIIB': KeuzelijstWaarde(invulwaarde='type-IIIB',
                                      label='type IIIB',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='type IIIB',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IIIB')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlSteenslagType.get_dummy_data()

