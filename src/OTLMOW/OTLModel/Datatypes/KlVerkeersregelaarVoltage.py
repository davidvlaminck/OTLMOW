# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


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
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarVoltage/230'),
        '40': KeuzelijstWaarde(invulwaarde='40',
                               label='40',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarVoltage/40'),
        '42': KeuzelijstWaarde(invulwaarde='42',
                               label='42',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarVoltage/42')
    }

