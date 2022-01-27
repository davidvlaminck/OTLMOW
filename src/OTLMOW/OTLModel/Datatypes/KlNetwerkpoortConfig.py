# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNetwerkpoortConfig(KeuzelijstField):
    """Lijst van mogelijke soort verbindingen aangeboden aan de klant van Netwerkpoorten."""
    naam = 'KlNetwerkpoortConfig'
    label = 'Netwerkpoort configuratie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerkpoortConfig'
    definition = 'Lijst van mogelijke soort verbindingen aangeboden aan de klant van Netwerkpoorten.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerkpoortConfig'
    options = {
        '100GE': KeuzelijstWaarde(invulwaarde='100GE',
                                  label='100GE',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/100GE'),
        '10GE': KeuzelijstWaarde(invulwaarde='10GE',
                                 label='10GE',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/10GE'),
        '16G-FC': KeuzelijstWaarde(invulwaarde='16G-FC',
                                   label='16G FC',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/16G-FC'),
        '1G-FC': KeuzelijstWaarde(invulwaarde='1G-FC',
                                  label='1G FC',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/1G-FC'),
        '40GE': KeuzelijstWaarde(invulwaarde='40GE',
                                 label='40GE',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/40GE'),
        '4G-FC': KeuzelijstWaarde(invulwaarde='4G-FC',
                                  label='4G FC',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/4G-FC'),
        '8G-FC': KeuzelijstWaarde(invulwaarde='8G-FC',
                                  label='8G FC',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/8G-FC'),
        'E': KeuzelijstWaarde(invulwaarde='E',
                              label='E',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/E'),
        'E1': KeuzelijstWaarde(invulwaarde='E1',
                               label='E1',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/E1'),
        'FE': KeuzelijstWaarde(invulwaarde='FE',
                               label='FE',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/FE'),
        'GE': KeuzelijstWaarde(invulwaarde='GE',
                               label='GE',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/GE'),
        'NULL': KeuzelijstWaarde(invulwaarde='NULL',
                                 label='NULL',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/NULL'),
        'OTU-1': KeuzelijstWaarde(invulwaarde='OTU-1',
                                  label='OTU-1',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/OTU-1'),
        'OTU-2': KeuzelijstWaarde(invulwaarde='OTU-2',
                                  label='OTU-2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/OTU-2'),
        'OTU-4': KeuzelijstWaarde(invulwaarde='OTU-4',
                                  label='OTU-4',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/OTU-4'),
        'Other': KeuzelijstWaarde(invulwaarde='Other',
                                  label='Other',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/Other'),
        'STM-1': KeuzelijstWaarde(invulwaarde='STM-1',
                                  label='STM-1',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/STM-1'),
        'STM-16': KeuzelijstWaarde(invulwaarde='STM-16',
                                   label='STM-16',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/STM-16'),
        'STM-4': KeuzelijstWaarde(invulwaarde='STM-4',
                                  label='STM-4',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/STM-4'),
        'STM-64': KeuzelijstWaarde(invulwaarde='STM-64',
                                   label='STM-64',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/STM-64')
    }

