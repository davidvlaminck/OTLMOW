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
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersregelaarVoltage'
    options = {
        '230': KeuzelijstWaarde(invulwaarde='230',
                                label='230',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarVoltage/230'),
        '40': KeuzelijstWaarde(invulwaarde='40',
                               label='40',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarVoltage/40'),
        '42': KeuzelijstWaarde(invulwaarde='42',
                               label='42',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarVoltage/42')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

