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
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTelecommunicationsAppurtenanceType'
    options = {
        'spliceclosure': KeuzelijstWaarde(invulwaarde='spliceclosure',
                                          label='spliceClosure',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecommunicationsAppurtenanceType/spliceclosure'),
        'termination': KeuzelijstWaarde(invulwaarde='termination',
                                        label='termination',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecommunicationsAppurtenanceType/termination')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

