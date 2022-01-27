# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLedVerlNiveau(KeuzelijstField):
    """Een set van verlichtingstechnische eisen zoals gemiddelde luminantie, verlichtingsterkte, uniformeiten."""
    naam = 'KlWvLedVerlNiveau'
    label = 'WV LED verlichtingsniveau'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedVerlNiveau'
    definition = 'Een set van verlichtingstechnische eisen zoals gemiddelde luminantie, verlichtingsterkte, uniformeiten.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedVerlNiveau'
    options = {
        'C1': KeuzelijstWaarde(invulwaarde='C1',
                               label='C1',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/C1'),
        'C2': KeuzelijstWaarde(invulwaarde='C2',
                               label='C2',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/C2'),
        'C3': KeuzelijstWaarde(invulwaarde='C3',
                               label='C3',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/C3'),
        'C4': KeuzelijstWaarde(invulwaarde='C4',
                               label='C4',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/C4'),
        'M2': KeuzelijstWaarde(invulwaarde='M2',
                               label='M2',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/M2'),
        'M3': KeuzelijstWaarde(invulwaarde='M3',
                               label='M3',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/M3'),
        'M4': KeuzelijstWaarde(invulwaarde='M4',
                               label='M4',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/M4'),
        'P3': KeuzelijstWaarde(invulwaarde='P3',
                               label='P3',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/P3'),
        'P4': KeuzelijstWaarde(invulwaarde='P4',
                               label='P4',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/P4'),
        'P5': KeuzelijstWaarde(invulwaarde='P5',
                               label='P5',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/P5'),
        'ZL': KeuzelijstWaarde(invulwaarde='ZL',
                               label='ZL',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/ZL'),
        'ZR': KeuzelijstWaarde(invulwaarde='ZR',
                               label='ZR',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/ZR')
    }

