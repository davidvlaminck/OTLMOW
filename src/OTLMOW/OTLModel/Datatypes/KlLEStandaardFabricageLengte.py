# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEStandaardFabricageLengte(KeuzelijstField):
    """De lengte van de inviduele kantopsluiting volgens de norm."""
    naam = 'KlLEStandaardFabricageLengte'
    label = 'Standaard frabricage lengte'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEStandaardFabricageLengte'
    definition = 'De lengte van de inviduele kantopsluiting volgens de norm.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEStandaardFabricageLengte'
    options = {
        '0.5-m': KeuzelijstWaarde(invulwaarde='0.5-m',
                                  label='0,5 m',
                                  definitie='De fabricagelengte is 0,5 meter.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEStandaardFabricageLengte/0.5-m'),
        '1-m': KeuzelijstWaarde(invulwaarde='1-m',
                                label='1 m',
                                definitie='De fabricagelengte is 1 meter.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEStandaardFabricageLengte/1-m')
    }

