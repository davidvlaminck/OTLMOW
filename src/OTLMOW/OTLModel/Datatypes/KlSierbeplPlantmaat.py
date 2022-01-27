# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSierbeplPlantmaat(KeuzelijstField):
    """De plantmaten van de sierplant."""
    naam = 'KlSierbeplPlantmaat'
    label = 'Sierbepl plantmaat'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSierbeplPlantmaat'
    definition = 'De plantmaten van de sierplant.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSierbeplPlantmaat'
    options = {
        '20-30': KeuzelijstWaarde(invulwaarde='20-30',
                                  label='20-30',
                                  definitie='20/30',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplPlantmaat/20-30'),
        '30-40': KeuzelijstWaarde(invulwaarde='30-40',
                                  label='30-40',
                                  definitie='30/40',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplPlantmaat/30-40'),
        '40-60': KeuzelijstWaarde(invulwaarde='40-60',
                                  label='40-60',
                                  definitie='40/60',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplPlantmaat/40-60')
    }

