# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZpadType(KeuzelijstField):
    """De soort verbinding, gebaseerd op het gebruikte protocol."""
    naam = 'KlZpadType'
    label = 'Z-pad type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlZpadType'
    definition = 'De soort verbinding, gebaseerd op het gebruikte protocol.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZpadType'
    options = {
        'E1': KeuzelijstWaarde(invulwaarde='E1',
                               label='E1',
                               definitie='E1 signaal is een TDM signaal van 2Mb/s, verdeeld in 64 kbit/s kanalen, vooral gebruikt voor telefonie en lage snelheid data transmissie.',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZpadType/E1'),
        'Ethernet': KeuzelijstWaarde(invulwaarde='Ethernet',
                                     label='Ethernet',
                                     definitie='Packet switched netwerkstandaard waarmee computers in een LAN met elkaar communiceren, via het MEF metro ethernet forum wordt gebruikte apparatuur gecertificeerd tegen de ethernet standaarden.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZpadType/Ethernet'),
        'FC': KeuzelijstWaarde(invulwaarde='FC',
                               label='FC',
                               definitie='Fibre Channel protocol, standaard, gebruikt voor Storage Area Netwerken.',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZpadType/FC'),
        'NULL': KeuzelijstWaarde(invulwaarde='NULL',
                                 label='NULL',
                                 definitie='niet ingevuld',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZpadType/NULL'),
        'Other': KeuzelijstWaarde(invulwaarde='Other',
                                  label='Other',
                                  definitie='Ander soort verbinding',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZpadType/Other')
    }

