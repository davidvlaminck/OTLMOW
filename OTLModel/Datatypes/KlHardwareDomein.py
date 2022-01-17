# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHardwareDomein(KeuzelijstField):
    """Lijst met gebruikte administratieve groeperingen van meerdere particuliere computernetwerken of hosts binnen dezelfde infrastructuur."""
    naam = 'KlHardwareDomein'
    label = 'Hardware domein'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlHardwareDomein'
    definition = 'Lijst met gebruikte administratieve groeperingen van meerdere particuliere computernetwerken of hosts binnen dezelfde infrastructuur.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHardwareDomein'
    options = {
        'alfa': KeuzelijstWaarde(invulwaarde='alfa',
                                 label='alfa',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareDomein/alfa'),
        'belfla': KeuzelijstWaarde(invulwaarde='belfla',
                                   label='belfla',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareDomein/belfla')
    }

