# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlClusterClusterdoel(KeuzelijstField):
    """De reden waarom de custer is opgezet."""
    naam = 'KlClusterClusterdoel'
    label = 'Cluster clusterdoel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlClusterClusterdoel'
    definition = 'De reden waarom de custer is opgezet.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlClusterClusterdoel'
    options = {
        'groeperen-resources': KeuzelijstWaarde(invulwaarde='groeperen-resources',
                                                label='groeperen resources',
                                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlClusterClusterdoel/groeperen-resources'),
        'redundantie': KeuzelijstWaarde(invulwaarde='redundantie',
                                        label='redundantie',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlClusterClusterdoel/redundantie')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlClusterClusterdoel.get_dummy_data()

