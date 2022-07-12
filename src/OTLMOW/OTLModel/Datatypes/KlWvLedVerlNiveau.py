# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLedVerlNiveau(KeuzelijstField):
    """Een set van verlichtingstechnische eisen zoals gemiddelde luminantie, verlichtingsterkte, uniformeiten."""
    naam = 'KlWvLedVerlNiveau'
    label = 'WV LED verlichtingsniveau'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedVerlNiveau'
    definition = 'Een set van verlichtingstechnische eisen zoals gemiddelde luminantie, verlichtingsterkte, uniformeiten.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedVerlNiveau'
    options = {
        'C1': KeuzelijstWaarde(invulwaarde='C1',
                               label='C1',
                               status='ingebruik',
                               definitie='C1',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/C1'),
        'C2': KeuzelijstWaarde(invulwaarde='C2',
                               label='C2',
                               status='ingebruik',
                               definitie='C2',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/C2'),
        'C3': KeuzelijstWaarde(invulwaarde='C3',
                               label='C3',
                               status='ingebruik',
                               definitie='C3',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/C3'),
        'C4': KeuzelijstWaarde(invulwaarde='C4',
                               label='C4',
                               status='ingebruik',
                               definitie='C4',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/C4'),
        'M2': KeuzelijstWaarde(invulwaarde='M2',
                               label='M2',
                               status='ingebruik',
                               definitie='M2',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/M2'),
        'M3': KeuzelijstWaarde(invulwaarde='M3',
                               label='M3',
                               status='ingebruik',
                               definitie='M3',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/M3'),
        'M4': KeuzelijstWaarde(invulwaarde='M4',
                               label='M4',
                               status='ingebruik',
                               definitie='M4',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/M4'),
        'P3': KeuzelijstWaarde(invulwaarde='P3',
                               label='P3',
                               status='ingebruik',
                               definitie='P3',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/P3'),
        'P4': KeuzelijstWaarde(invulwaarde='P4',
                               label='P4',
                               status='ingebruik',
                               definitie='P4',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/P4'),
        'P5': KeuzelijstWaarde(invulwaarde='P5',
                               label='P5',
                               status='ingebruik',
                               definitie='P5',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/P5'),
        'ZL': KeuzelijstWaarde(invulwaarde='ZL',
                               label='ZL',
                               status='ingebruik',
                               definitie='ZL',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/ZL'),
        'ZR': KeuzelijstWaarde(invulwaarde='ZR',
                               label='ZR',
                               status='ingebruik',
                               definitie='ZR',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/ZR'),
        'zl3': KeuzelijstWaarde(invulwaarde='zl3',
                                label='ZL3',
                                status='ingebruik',
                                definitie='ZL3',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/zl3'),
        'zl4': KeuzelijstWaarde(invulwaarde='zl4',
                                label='ZL4',
                                status='ingebruik',
                                definitie='ZL4',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/zl4'),
        'zr3': KeuzelijstWaarde(invulwaarde='zr3',
                                label='ZR3',
                                status='ingebruik',
                                definitie='ZR3',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/zr3'),
        'zr4': KeuzelijstWaarde(invulwaarde='zr4',
                                label='ZR4',
                                status='ingebruik',
                                definitie='ZR4',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedVerlNiveau/zr4')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlWvLedVerlNiveau.get_dummy_data()

