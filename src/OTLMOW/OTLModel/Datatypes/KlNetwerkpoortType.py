# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNetwerkpoortType(KeuzelijstField):
    """Lijst van types voor Netwerkpoort."""
    naam = 'KlNetwerkpoortType'
    label = 'Netwerkpoort type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerkpoortType'
    definition = 'Lijst van types voor Netwerkpoort.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerkpoortType'
    options = {
        'NNI': KeuzelijstWaarde(invulwaarde='NNI',
                                label='NNI',
                                definitie='Network-Network-Interface: deze poort verbindt het netwerk toestel met een poort van een ander netwerk toestel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortType/NNI'),
        'NULL': KeuzelijstWaarde(invulwaarde='NULL',
                                 label='NULL',
                                 definitie='Geen interface.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortType/NULL'),
        'Other': KeuzelijstWaarde(invulwaarde='Other',
                                  label='Other',
                                  definitie='Ander, onbekend type interface.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortType/Other'),
        'UNI': KeuzelijstWaarde(invulwaarde='UNI',
                                label='UNI',
                                definitie='User-Network-Interface: deze poort verbindt het netwerk toestel met de poort van een gebruiker.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortType/UNI'),
        'ncni': KeuzelijstWaarde(invulwaarde='ncni',
                                 label='NCNI',
                                 definitie='Een Not Configured Network Interface.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortType/ncni')
    }

