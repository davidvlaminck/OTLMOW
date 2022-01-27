# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLedTussenafstand(KeuzelijstField):
    """Afstand tussen de verschillende LED verlichtingstoestellen."""
    naam = 'KlWvLedTussenafstand'
    label = 'WV LED tussenafstand'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedTussenafstand'
    definition = 'Afstand tussen de verschillende LED verlichtingstoestellen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedTussenafstand'
    options = {
        'S015': KeuzelijstWaarde(invulwaarde='S015',
                                 label='S015',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S015'),
        'S020': KeuzelijstWaarde(invulwaarde='S020',
                                 label='S020',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S020'),
        'S025': KeuzelijstWaarde(invulwaarde='S025',
                                 label='S025',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S025'),
        'S030': KeuzelijstWaarde(invulwaarde='S030',
                                 label='S030',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S030'),
        'S035': KeuzelijstWaarde(invulwaarde='S035',
                                 label='S035',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S035'),
        'S040': KeuzelijstWaarde(invulwaarde='S040',
                                 label='S040',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S040'),
        'S045': KeuzelijstWaarde(invulwaarde='S045',
                                 label='S045',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S045'),
        'S050': KeuzelijstWaarde(invulwaarde='S050',
                                 label='S050',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S050'),
        'S060': KeuzelijstWaarde(invulwaarde='S060',
                                 label='S060',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S060'),
        'S070': KeuzelijstWaarde(invulwaarde='S070',
                                 label='S070',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S070'),
        'S080': KeuzelijstWaarde(invulwaarde='S080',
                                 label='S080',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S080'),
        'S090': KeuzelijstWaarde(invulwaarde='S090',
                                 label='S090',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S090'),
        'S100': KeuzelijstWaarde(invulwaarde='S100',
                                 label='S100',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedTussenafstand/S100')
    }

