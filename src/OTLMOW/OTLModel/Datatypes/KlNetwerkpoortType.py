# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNetwerkpoortType(KeuzelijstField):
    """Lijst van types voor Netwerkpoort."""
    naam = 'KlNetwerkpoortType'
    label = 'Netwerkpoort type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerkpoortType'
    definition = 'Lijst van types voor Netwerkpoort.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerkpoortType'
    options = {
        'NNI': KeuzelijstWaarde(invulwaarde='NNI',
                                label='NNI',
                                status='ingebruik',
                                definitie='Network-Network-Interface: deze poort verbindt het netwerk toestel met een poort van een ander netwerk toestel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortType/NNI'),
        'NULL': KeuzelijstWaarde(invulwaarde='NULL',
                                 label='NULL',
                                 status='ingebruik',
                                 definitie='Geen interface.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortType/NULL'),
        'Other': KeuzelijstWaarde(invulwaarde='Other',
                                  label='Other',
                                  status='ingebruik',
                                  definitie='Ander, onbekend type interface.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortType/Other'),
        'UNI': KeuzelijstWaarde(invulwaarde='UNI',
                                label='UNI',
                                status='ingebruik',
                                definitie='User-Network-Interface: deze poort verbindt het netwerk toestel met de poort van een gebruiker.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortType/UNI'),
        'ncni': KeuzelijstWaarde(invulwaarde='ncni',
                                 label='NCNI',
                                 status='ingebruik',
                                 definitie='Een Not Configured Network Interface.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortType/ncni')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

