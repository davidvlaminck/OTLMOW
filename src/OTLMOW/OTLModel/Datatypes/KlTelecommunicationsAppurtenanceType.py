# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTelecommunicationsAppurtenanceType(KeuzelijstField):
    """Lijst van types voor telecommunications appurtenance."""
    naam = 'KlTelecommunicationsAppurtenanceType'
    label = 'Telecommunications appurtenance type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlTelecommunicationsAppurtenanceType'
    definition = 'Lijst van types voor telecommunications appurtenance.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTelecommunicationsAppurtenanceType'
    options = {
        'spliceclosure': KeuzelijstWaarde(invulwaarde='spliceclosure',
                                          label='spliceClosure',
                                          status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecommunicationsAppurtenanceType/spliceclosure'),
        'termination': KeuzelijstWaarde(invulwaarde='termination',
                                        label='termination',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecommunicationsAppurtenanceType/termination')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlTelecommunicationsAppurtenanceType.get_dummy_data()

