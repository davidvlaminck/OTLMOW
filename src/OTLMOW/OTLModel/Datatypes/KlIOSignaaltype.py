# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIOSignaaltype(KeuzelijstField):
    """Geeft aan of de IO-kaart werkt met een digitaal of met een analoog signaal."""
    naam = 'KlIOSignaaltype'
    label = 'IO-kaart signaaltype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIOSignaaltype'
    definition = 'Geeft aan of de IO-kaart werkt met een digitaal of met een analoog signaal.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIOSignaaltype'
    options = {
        'analoog': KeuzelijstWaarde(invulwaarde='analoog',
                                    label='analoog',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOSignaaltype/analoog'),
        'digitaal': KeuzelijstWaarde(invulwaarde='digitaal',
                                     label='digitaal',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOSignaaltype/digitaal')
    }

