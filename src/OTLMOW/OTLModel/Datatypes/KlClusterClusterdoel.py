# coding=utf-8
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
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlClusterClusterdoel/groeperen-resources'),
        'redundantie': KeuzelijstWaarde(invulwaarde='redundantie',
                                        label='redundantie',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlClusterClusterdoel/redundantie')
    }

