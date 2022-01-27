# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLedOverhang(KeuzelijstField):
    """Afstand tot de rand van de rijbaan van de verticale projectie van het verlichtingstoestel op de rijbaan in meter. Als de afstand tot de rijbaan gelijk is aan 0, dan valt de verticale projectie samen met de rand van de rijbaan, bij negatieve waardes ligt de verticale projectie in de berm en bij positieve waardes ligt de verticale projectie op de rijbaan."""
    naam = 'KlWvLedOverhang'
    label = 'WV LED overhang'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedOverhang'
    definition = 'Afstand tot de rand van de rijbaan van de verticale projectie van het verlichtingstoestel op de rijbaan in meter. Als de afstand tot de rijbaan gelijk is aan 0, dan valt de verticale projectie samen met de rand van de rijbaan, bij negatieve waardes ligt de verticale projectie in de berm en bij positieve waardes ligt de verticale projectie op de rijbaan.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedOverhang'
    options = {
        'o+0': KeuzelijstWaarde(invulwaarde='o+0',
                                label='o+0',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+0'),
        'o+0.5': KeuzelijstWaarde(invulwaarde='o+0.5',
                                  label='o+0.5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+0.5'),
        'o+1.5': KeuzelijstWaarde(invulwaarde='o+1.5',
                                  label='o+1.5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+1.5'),
        'o+2.5': KeuzelijstWaarde(invulwaarde='o+2.5',
                                  label='o+2.5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+2.5'),
        'o+3.5': KeuzelijstWaarde(invulwaarde='o+3.5',
                                  label='o+3.5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+3.5'),
        'o+4.5': KeuzelijstWaarde(invulwaarde='o+4.5',
                                  label='o+4.5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+4.5'),
        'o-1': KeuzelijstWaarde(invulwaarde='o-1',
                                label='o-1',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-1'),
        'o-2': KeuzelijstWaarde(invulwaarde='o-2',
                                label='o-2',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-2'),
        'o-3': KeuzelijstWaarde(invulwaarde='o-3',
                                label='o-3',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-3'),
        'o-4': KeuzelijstWaarde(invulwaarde='o-4',
                                label='o-4',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-4'),
        'o-5': KeuzelijstWaarde(invulwaarde='o-5',
                                label='o-5',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-5')
    }

