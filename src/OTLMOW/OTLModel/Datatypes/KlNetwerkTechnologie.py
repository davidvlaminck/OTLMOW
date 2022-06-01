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
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerkTechnologie'
    options = {
        'CEN': KeuzelijstWaarde(invulwaarde='CEN',
                                label='CEN',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/CEN'),
        'NULL': KeuzelijstWaarde(invulwaarde='NULL',
                                 label='NULL',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/NULL'),
        'OTN': KeuzelijstWaarde(invulwaarde='OTN',
                                label='OTN',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/OTN'),
        'Other': KeuzelijstWaarde(invulwaarde='Other',
                                  label='Other',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/Other'),
        'PDH': KeuzelijstWaarde(invulwaarde='PDH',
                                label='PDH',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/PDH'),
        'SDH': KeuzelijstWaarde(invulwaarde='SDH',
                                label='SDH',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/SDH'),
        'WDM': KeuzelijstWaarde(invulwaarde='WDM',
                                label='WDM',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/WDM'),
        'Wireless': KeuzelijstWaarde(invulwaarde='Wireless',
                                     label='Wireless',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/Wireless')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlNetwerkTechnologie.get_dummy_data()

