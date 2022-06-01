# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEnergiemeterMetertype(KeuzelijstField):
    """Type meter (mechanisch, elektronisch)."""
    naam = 'KlEnergiemeterMetertype'
    label = 'Elektrisch metertype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlEnergiemeterMetertype'
    definition = 'Type meter (mechanisch, elektronisch).'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEnergiemeterMetertype'
    options = {
        'elektronisch': KeuzelijstWaarde(invulwaarde='elektronisch',
                                         label='elektronisch',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEnergiemeterMetertype/elektronisch'),
        'mechanisch': KeuzelijstWaarde(invulwaarde='mechanisch',
                                       label='mechanisch',
                                       definitie='Nakijken bij EVT',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEnergiemeterMetertype/mechanisch')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlEnergiemeterMetertype.get_dummy_data()

