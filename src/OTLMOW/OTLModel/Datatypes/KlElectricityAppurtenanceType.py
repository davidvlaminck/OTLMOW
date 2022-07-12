# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlElectricityAppurtenanceType(KeuzelijstField):
    """Lijst voor types  van de ElectricityAppurtenance."""
    naam = 'KlElectricityAppurtenanceType'
    label = 'Electricity appurtenance type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlElectricityAppurtenanceType'
    definition = 'Lijst voor types  van de ElectricityAppurtenance.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlElectricityAppurtenanceType'
    options = {
        'aarding': KeuzelijstWaarde(invulwaarde='aarding',
                                    label='aarding',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElectricityAppurtenanceType/aarding'),
        'deliverypoint': KeuzelijstWaarde(invulwaarde='deliverypoint',
                                          label='deliveryPoint',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElectricityAppurtenanceType/deliverypoint'),
        'mof': KeuzelijstWaarde(invulwaarde='mof',
                                label='mof',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElectricityAppurtenanceType/mof'),
        'streetlight': KeuzelijstWaarde(invulwaarde='streetlight',
                                        label='streetLight',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElectricityAppurtenanceType/streetlight')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlElectricityAppurtenanceType.get_dummy_data()

