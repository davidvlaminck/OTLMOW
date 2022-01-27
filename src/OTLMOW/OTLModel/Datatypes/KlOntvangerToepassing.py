# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOntvangerToepassing(KeuzelijstField):
    """Keuzelijst met modelnamen voor OntvangerToepassing."""
    naam = 'KlOntvangerToepassing'
    label = 'Ontvanger toepassing'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOntvangerToepassing'
    definition = 'Keuzelijst met modelnamen voor OntvangerToepassing.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOntvangerToepassing'
    options = {
        'GPRS': KeuzelijstWaarde(invulwaarde='GPRS',
                                 label='GPRS',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOntvangerToepassing/GPRS'),
        'GSM': KeuzelijstWaarde(invulwaarde='GSM',
                                label='GSM',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOntvangerToepassing/GSM'),
        'KAR': KeuzelijstWaarde(invulwaarde='KAR',
                                label='KAR',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOntvangerToepassing/KAR'),
        'WIFI': KeuzelijstWaarde(invulwaarde='WIFI',
                                 label='WIFI',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOntvangerToepassing/WIFI')
    }

