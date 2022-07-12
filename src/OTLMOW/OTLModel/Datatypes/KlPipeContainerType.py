# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPipeContainerType(KeuzelijstField):
    """Lijst met types van pies voor het oude AKELA-type Pipe."""
    naam = 'KlPipeContainerType'
    label = 'Pipe container type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlPipeContainerType'
    definition = 'Lijst met types van pies voor het oude AKELA-type Pipe.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPipeContainerType'
    options = {
        'kabelenleidinggoot': KeuzelijstWaarde(invulwaarde='kabelenleidinggoot',
                                               label='kabelEnLeidingGoot',
                                               status='ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPipeContainerType/kabelenleidinggoot'),
        'mantelbuis': KeuzelijstWaarde(invulwaarde='mantelbuis',
                                       label='mantelbuis',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPipeContainerType/mantelbuis')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlPipeContainerType.get_dummy_data()

