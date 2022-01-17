# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


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

