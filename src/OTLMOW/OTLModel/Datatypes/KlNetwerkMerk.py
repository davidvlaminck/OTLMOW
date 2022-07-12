# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNetwerkMerk(KeuzelijstField):
    """Merknamen voor Netwerkelementen."""
    naam = 'KlNetwerkMerk'
    label = 'Netwerkelement merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerkMerk'
    definition = 'Merknamen voor Netwerkelementen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerkMerk'
    options = {
        'ABB': KeuzelijstWaarde(invulwaarde='ABB',
                                label='ABB',
                                status='ingebruik',
                                definitie='ABB',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/ABB'),
        'Ciena': KeuzelijstWaarde(invulwaarde='Ciena',
                                  label='Ciena',
                                  status='ingebruik',
                                  definitie='Ciena',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/Ciena'),
        'Cisco': KeuzelijstWaarde(invulwaarde='Cisco',
                                  label='Cisco',
                                  status='ingebruik',
                                  definitie='Cisco',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/Cisco'),
        'HP': KeuzelijstWaarde(invulwaarde='HP',
                               label='HP',
                               status='ingebruik',
                               definitie='HP',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/HP'),
        'NOKIA': KeuzelijstWaarde(invulwaarde='NOKIA',
                                  label='NOKIA',
                                  status='ingebruik',
                                  definitie='NOKIA',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/NOKIA'),
        'NULL': KeuzelijstWaarde(invulwaarde='NULL',
                                 label='NULL',
                                 status='ingebruik',
                                 definitie='null',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/NULL'),
        'Other': KeuzelijstWaarde(invulwaarde='Other',
                                  label='Other',
                                  status='ingebruik',
                                  definitie='Andere',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/Other'),
        'Proxim': KeuzelijstWaarde(invulwaarde='Proxim',
                                   label='Proxim',
                                   status='ingebruik',
                                   definitie='Proxim',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/Proxim'),
        'actelis': KeuzelijstWaarde(invulwaarde='actelis',
                                    label='Actelis',
                                    status='ingebruik',
                                    definitie='Actelis',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/actelis'),
        'fortinet': KeuzelijstWaarde(invulwaarde='fortinet',
                                     label='Fortinet',
                                     status='ingebruik',
                                     definitie='Fortinet',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/fortinet'),
        'hirschmann': KeuzelijstWaarde(invulwaarde='hirschmann',
                                       label='Hirschmann',
                                       status='ingebruik',
                                       definitie='Hirschmann',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/hirschmann')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlNetwerkMerk.get_dummy_data()

