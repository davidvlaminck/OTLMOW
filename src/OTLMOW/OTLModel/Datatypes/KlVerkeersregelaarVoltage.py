# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersregelaarVoltage(KeuzelijstField):
    """Keuzelijst met de voorkomende voltages gebruikt voor verkeersregelaars."""
    naam = 'KlVerkeersregelaarVoltage'
    label = 'Verkeersregelaar voltage'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersregelaarVoltage'
    definition = 'Keuzelijst met de voorkomende voltages gebruikt voor verkeersregelaars.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersregelaarVoltage'
    options = {
        '230': KeuzelijstWaarde(invulwaarde='230',
                                label='230',
                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarVoltage/230'),
        '40': KeuzelijstWaarde(invulwaarde='40',
                               label='40',
                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarVoltage/40'),
        '42': KeuzelijstWaarde(invulwaarde='42',
                               label='42',
                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarVoltage/42')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlVerkeersregelaarVoltage.get_dummy_data()

