# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLedLichtpunthoogte(KeuzelijstField):
    """Hoogte van het lichtpunt ten opzichte van de rijweg."""
    naam = 'KlWvLedLichtpunthoogte'
    label = 'WV LED lichtpunthoogte'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedLichtpunthoogte'
    definition = 'Hoogte van het lichtpunt ten opzichte van de rijweg.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedLichtpunthoogte'
    options = {
        'H04': KeuzelijstWaarde(invulwaarde='H04',
                                label='H04',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H04'),
        'H05': KeuzelijstWaarde(invulwaarde='H05',
                                label='H05',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H05'),
        'H06': KeuzelijstWaarde(invulwaarde='H06',
                                label='H06',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H06'),
        'H08': KeuzelijstWaarde(invulwaarde='H08',
                                label='H08',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H08'),
        'H10': KeuzelijstWaarde(invulwaarde='H10',
                                label='H10',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H10'),
        'H12': KeuzelijstWaarde(invulwaarde='H12',
                                label='H12',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H12'),
        'H16': KeuzelijstWaarde(invulwaarde='H16',
                                label='H16',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H16'),
        'H18': KeuzelijstWaarde(invulwaarde='H18',
                                label='H18',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H18'),
        'H20': KeuzelijstWaarde(invulwaarde='H20',
                                label='H20',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtpunthoogte/H20')
    }

