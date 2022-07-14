# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSierbeplPlantmaat(KeuzelijstField):
    """De plantmaten van de sierplant."""
    naam = 'KlSierbeplPlantmaat'
    label = 'Sierbepl plantmaat'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSierbeplPlantmaat'
    definition = 'De plantmaten van de sierplant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSierbeplPlantmaat'
    options = {
        '20-30': KeuzelijstWaarde(invulwaarde='20-30',
                                  label='20-30',
                                  status='ingebruik',
                                  definitie='20/30',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplPlantmaat/20-30'),
        '30-40': KeuzelijstWaarde(invulwaarde='30-40',
                                  label='30-40',
                                  status='ingebruik',
                                  definitie='30/40',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplPlantmaat/30-40'),
        '40-60': KeuzelijstWaarde(invulwaarde='40-60',
                                  label='40-60',
                                  status='ingebruik',
                                  definitie='40/60',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplPlantmaat/40-60')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

