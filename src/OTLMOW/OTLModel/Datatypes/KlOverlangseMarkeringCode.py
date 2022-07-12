# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOverlangseMarkeringCode(KeuzelijstField):
    """Codes van de overlangse markering."""
    naam = 'KlOverlangseMarkeringCode'
    label = 'Overlangse markering code'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOverlangseMarkeringCode'
    definition = 'Codes van de overlangse markering.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOverlangseMarkeringCode'
    options = {
        'BAD-0.20': KeuzelijstWaarde(invulwaarde='BAD-0.20',
                                     label='BAD 0.20',
                                     status='ingebruik',
                                     definitie='Doorlopende overlangse bushalte aslijn markering (0.2 meter breedte).',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/BAD-0.20'),
        'BAD-0.30': KeuzelijstWaarde(invulwaarde='BAD-0.30',
                                     label='BAD 0.30',
                                     status='ingebruik',
                                     definitie='Doorlopende overlangse bushalte aslijn markering (0.3 meter breedte).',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/BAD-0.30'),
        'BAO-0.30-x-2.50-(1)': KeuzelijstWaarde(invulwaarde='BAO-0.30-x-2.50-(1)',
                                                label='BAO 0.30 x 2.50 (1)',
                                                status='ingebruik',
                                                definitie='Onderbroken overlangse bushalte aslijn markering (0.3 meter breedte en 2.5 meter lengte).',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/BAO-0.30-x-2.50-(1)'),
        'FAD-0.15': KeuzelijstWaarde(invulwaarde='FAD-0.15',
                                     label='FAD 0.15',
                                     status='ingebruik',
                                     definitie='Doorlopende overlangse fietspad aslijn markering.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/FAD-0.15'),
        'FAO-0.15-x-1.25-(1.25)': KeuzelijstWaarde(invulwaarde='FAO-0.15-x-1.25-(1.25)',
                                                   label='FAO 0.15 x 1.25 (1.25)',
                                                   status='ingebruik',
                                                   definitie='Onderbroken overlangse fietspad aslijn markering.',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/FAO-0.15-x-1.25-(1.25)'),
        'FAO-0.15-x-1.25-(3.25)': KeuzelijstWaarde(invulwaarde='FAO-0.15-x-1.25-(3.25)',
                                                   label='FAO 0.15 x 1.25 (3.25)',
                                                   status='ingebruik',
                                                   definitie='Onderbroken overlangse fietspad aslijn markering.',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/FAO-0.15-x-1.25-(3.25)'),
        'FRO-0.15-x-1.25-(1.25)': KeuzelijstWaarde(invulwaarde='FRO-0.15-x-1.25-(1.25)',
                                                   label='FRO 0.15 x 1.25 (1.25)',
                                                   status='ingebruik',
                                                   definitie='Onderbroken overlangse fietspad randlijn markering.',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/FRO-0.15-x-1.25-(1.25)'),
        'FRO-0.15-x-1.25-(3.75)': KeuzelijstWaarde(invulwaarde='FRO-0.15-x-1.25-(3.75)',
                                                   label='FRO 0.15 x 1.25 (3.75)',
                                                   status='ingebruik',
                                                   definitie='Onderbroken overlangse fietspad randlijn markering.',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/FRO-0.15-x-1.25-(3.75)'),
        'PRD-0.10': KeuzelijstWaarde(invulwaarde='PRD-0.10',
                                     label='PRD 0.10',
                                     status='ingebruik',
                                     definitie='Doorlopende overlangse randlijn parkeerstrook markering.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/PRD-0.10'),
        'RAD-0.15': KeuzelijstWaarde(invulwaarde='RAD-0.15',
                                     label='RAD 0.15',
                                     status='ingebruik',
                                     definitie='Doorlopende overlange markering (0.15 meter breedte).',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/RAD-0.15'),
        'RAD-0.20': KeuzelijstWaarde(invulwaarde='RAD-0.20',
                                     label='RAD 0.20',
                                     status='ingebruik',
                                     definitie='Doorlopende overlange markering (0.2 meter breedte).',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/RAD-0.20'),
        'RAO-0.15-x-1.00-(1.5)': KeuzelijstWaarde(invulwaarde='RAO-0.15-x-1.00-(1.5)',
                                                  label='RAO 0.15 x 1.00 (1.5)',
                                                  status='ingebruik',
                                                  definitie='Onderbroken overlangse aslijn markering (1.5 meter tussenruimte)',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/RAO-0.15-x-1.00-(1.5)'),
        'RAO-0.15-x-2.50-(10)': KeuzelijstWaarde(invulwaarde='RAO-0.15-x-2.50-(10)',
                                                 label='RAO 0.15 x 2.50 (10)',
                                                 status='ingebruik',
                                                 definitie='Onderbroken overlangse aslijn markering (10 meter tussenruimte)',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/RAO-0.15-x-2.50-(10)'),
        'RAO-0.20-x-1.00-(1.5)': KeuzelijstWaarde(invulwaarde='RAO-0.20-x-1.00-(1.5)',
                                                  label='RAO 0.20 x 1.00 (1.5)',
                                                  status='ingebruik',
                                                  definitie='Onderbroken overlangse aslijn markering (1.5 meter tussenruimte)',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/RAO-0.20-x-1.00-(1.5)'),
        'RAO-0.20-x-2.50-(10)': KeuzelijstWaarde(invulwaarde='RAO-0.20-x-2.50-(10)',
                                                 label='RAO 0.20 x 2.50 (10)',
                                                 status='ingebruik',
                                                 definitie='Onderbroken overlangse aslijn markering (10 meter tussenruimte)',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/RAO-0.20-x-2.50-(10)'),
        'RAO-0.30-x-1.00-(1.5)': KeuzelijstWaarde(invulwaarde='RAO-0.30-x-1.00-(1.5)',
                                                  label='RAO 0.30 x 1.00 (1.5)',
                                                  status='ingebruik',
                                                  definitie='Onderbroken overlangse aslijn markering (1.5 meter tussenruimte)',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/RAO-0.30-x-1.00-(1.5)'),
        'RRD-0.15': KeuzelijstWaarde(invulwaarde='RRD-0.15',
                                     label='RRD 0.15',
                                     status='ingebruik',
                                     definitie='Doorlopende overlangse randlijn markering (0.15 meter breedte)',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/RRD-0.15'),
        'RRD-0.20': KeuzelijstWaarde(invulwaarde='RRD-0.20',
                                     label='RRD 0.20',
                                     status='ingebruik',
                                     definitie='Doorlopende overlangse randlijn markering (0.20 meter breedte)',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/RRD-0.20'),
        'RRD-0.25': KeuzelijstWaarde(invulwaarde='RRD-0.25',
                                     label='RRD 0.25',
                                     status='ingebruik',
                                     definitie='Doorlopende overlangse randlijn markering (0.25 meter breedte)',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/RRD-0.25'),
        'RRD-0.30': KeuzelijstWaarde(invulwaarde='RRD-0.30',
                                     label='RRD 0.30',
                                     status='ingebruik',
                                     definitie='Doorlopende overlangse randlijn markering (0.30 meter breedte)',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/RRD-0.30'),
        'SAO-0.20-x-10-(2.5)': KeuzelijstWaarde(invulwaarde='SAO-0.20-x-10-(2.5)',
                                                label='SAO 0.20 x 10 (2.5)',
                                                status='ingebruik',
                                                definitie='Onderbroken overlangse aslijn spitsstrook markering.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangseMarkeringCode/SAO-0.20-x-10-(2.5)')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlOverlangseMarkeringCode.get_dummy_data()

