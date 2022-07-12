# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNetwerkTechnologie(KeuzelijstField):
    """Lijst van mogelijke intern gebruikte netwerk protocollen."""
    naam = 'KlNetwerkTechnologie'
    label = 'Netwerk technologie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerkTechnologie'
    definition = 'Lijst van mogelijke intern gebruikte netwerk protocollen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerkTechnologie'
    options = {
        'CEN': KeuzelijstWaarde(invulwaarde='CEN',
                                label='CEN',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/CEN'),
        'NULL': KeuzelijstWaarde(invulwaarde='NULL',
                                 label='NULL',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/NULL'),
        'OTN': KeuzelijstWaarde(invulwaarde='OTN',
                                label='OTN',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/OTN'),
        'Other': KeuzelijstWaarde(invulwaarde='Other',
                                  label='Other',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/Other'),
        'PDH': KeuzelijstWaarde(invulwaarde='PDH',
                                label='PDH',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/PDH'),
        'SDH': KeuzelijstWaarde(invulwaarde='SDH',
                                label='SDH',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/SDH'),
        'WDM': KeuzelijstWaarde(invulwaarde='WDM',
                                label='WDM',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/WDM'),
        'Wireless': KeuzelijstWaarde(invulwaarde='Wireless',
                                     label='Wireless',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/Wireless')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlNetwerkTechnologie.get_dummy_data()

