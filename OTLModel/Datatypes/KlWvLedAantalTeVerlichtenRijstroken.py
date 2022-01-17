# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLedAantalTeVerlichtenRijstroken(KeuzelijstField):
    """Het aantal rijstroken dat verlicht wordt door het LED verlichtingstoestel."""
    naam = 'KlWvLedAantalTeVerlichtenRijstroken'
    label = 'WV LED aantal te verlichten rijstroken'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedAantalTeVerlichtenRijstroken'
    definition = 'Het aantal rijstroken dat verlicht wordt door het LED verlichtingstoestel.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedAantalTeVerlichtenRijstroken'
    options = {
        'R1': KeuzelijstWaarde(invulwaarde='R1',
                               label='R1',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R1'),
        'R2': KeuzelijstWaarde(invulwaarde='R2',
                               label='R2',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R2'),
        'R3': KeuzelijstWaarde(invulwaarde='R3',
                               label='R3',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R3'),
        'R4': KeuzelijstWaarde(invulwaarde='R4',
                               label='R4',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R4'),
        'R5': KeuzelijstWaarde(invulwaarde='R5',
                               label='R5',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R5'),
        'R6': KeuzelijstWaarde(invulwaarde='R6',
                               label='R6',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R6')
    }

