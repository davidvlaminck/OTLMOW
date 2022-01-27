# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLetterVerschaaldType(KeuzelijstField):
    """De mogelijke types van een individueel verschaalde lettermarkering."""
    naam = 'KlLetterVerschaaldType'
    label = 'Type van de verschaalde letter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLetterVerschaaldType'
    definition = 'De mogelijke types van een individueel verschaalde lettermarkering.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLetterVerschaaldType'
    options = {
        'versmald---Hoofdletters-(basishoogte-0.4-meter)': KeuzelijstWaarde(invulwaarde='versmald---Hoofdletters-(basishoogte-0.4-meter)',
                                                                            label='versmald - Hoofdletters (basishoogte 0.4 meter)',
                                                                            definitie='Versmalde hoofdletters bij verschaling (basishoogte 0.4 meter)',
                                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaaldType/versmald---Hoofdletters-(basishoogte-0.4-meter)')
    }

