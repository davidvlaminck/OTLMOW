# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNetwerkMerk(KeuzelijstField):
    """Merknamen voor Netwerkelementen."""
    naam = 'KlNetwerkMerk'
    label = 'Netwerkelement merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerkMerk'
    definition = 'Merknamen voor Netwerkelementen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerkMerk'
    options = {
        'ABB': KeuzelijstWaarde(invulwaarde='ABB',
                                label='ABB',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/ABB'),
        'Ciena': KeuzelijstWaarde(invulwaarde='Ciena',
                                  label='Ciena',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/Ciena'),
        'Cisco': KeuzelijstWaarde(invulwaarde='Cisco',
                                  label='Cisco',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/Cisco'),
        'HP': KeuzelijstWaarde(invulwaarde='HP',
                               label='HP',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/HP'),
        'NOKIA': KeuzelijstWaarde(invulwaarde='NOKIA',
                                  label='NOKIA',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/NOKIA'),
        'NULL': KeuzelijstWaarde(invulwaarde='NULL',
                                 label='NULL',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/NULL'),
        'Other': KeuzelijstWaarde(invulwaarde='Other',
                                  label='Other',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/Other'),
        'Proxim': KeuzelijstWaarde(invulwaarde='Proxim',
                                   label='Proxim',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/Proxim')
    }

