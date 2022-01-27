# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPadNetwerkprotectie(KeuzelijstField):
    """Lijst van referenties van paden die redundantie kunnen leveren aan een Pad."""
    naam = 'KlPadNetwerkprotectie'
    label = 'Pad netwerkprotectie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlPadNetwerkprotectie'
    definition = 'Lijst van referenties van paden die redundantie kunnen leveren aan een Pad.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPadNetwerkprotectie'
    options = {
        'Customer': KeuzelijstWaarde(invulwaarde='Customer',
                                     label='Customer',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/Customer'),
        'LACP': KeuzelijstWaarde(invulwaarde='LACP',
                                 label='LACP',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/LACP'),
        'LCAS': KeuzelijstWaarde(invulwaarde='LCAS',
                                 label='LCAS',
                                 definitie='Link Capacity Adjustment Scheme (Enkel bij SDH)',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/LCAS'),
        'MPLS-TP': KeuzelijstWaarde(invulwaarde='MPLS-TP',
                                    label='MPLS-TP',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/MPLS-TP'),
        'MSSpring': KeuzelijstWaarde(invulwaarde='MSSpring',
                                     label='MSSpring',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/MSSpring'),
        'NULL': KeuzelijstWaarde(invulwaarde='NULL',
                                 label='NULL',
                                 definitie='geen systeembeveiliging',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/NULL'),
        'None': KeuzelijstWaarde(invulwaarde='None',
                                 label='None',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/None'),
        'OPS': KeuzelijstWaarde(invulwaarde='OPS',
                                label='OPS',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/OPS'),
        'Other': KeuzelijstWaarde(invulwaarde='Other',
                                  label='Other',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/Other'),
        'SNCP': KeuzelijstWaarde(invulwaarde='SNCP',
                                 label='SNCP',
                                 definitie='Sub Network Connection Protection (Bij OTN en SDH)',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/SNCP'),
        'STP': KeuzelijstWaarde(invulwaarde='STP',
                                label='STP',
                                definitie='Carrier Ethernet',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/STP')
    }

