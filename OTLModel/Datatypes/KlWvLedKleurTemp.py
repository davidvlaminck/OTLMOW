# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLedKleurTemp(KeuzelijstField):
    """Kleurtemperatuur van de LED's."""
    naam = 'KlWvLedKleurTemp'
    label = 'WV LED kleurtemperatuur'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedKleurTemp'
    definition = "Kleurtemperatuur van de LED's."
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedKleurTemp'
    options = {
        '1700': KeuzelijstWaarde(invulwaarde='1700',
                                 label='1700',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedKleurTemp/1700'),
        '2900': KeuzelijstWaarde(invulwaarde='2900',
                                 label='2900',
                                 definitie='/ CLASS : VPLMAST',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedKleurTemp/2900'),
        '4000': KeuzelijstWaarde(invulwaarde='4000',
                                 label='4000',
                                 definitie='/ CLASS : VPLMAST',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedKleurTemp/4000')
    }

