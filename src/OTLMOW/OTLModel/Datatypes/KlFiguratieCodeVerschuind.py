# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFiguratieCodeVerschuind(KeuzelijstField):
    """Codes voor de verschuinde figuratie markering."""
    naam = 'KlFiguratieCodeVerschuind'
    label = 'Figuratie code verschuind'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFiguratieCodeVerschuind'
    definition = 'Codes voor de verschuinde figuratie markering.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFiguratieCodeVerschuind'
    options = {
        'STOP-SmSc': KeuzelijstWaarde(invulwaarde='STOP-SmSc',
                                      label='STOP-SmSc',
                                      definitie='Een STOP markering smal en schuin.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCodeVerschuind/STOP-SmSc'),
        'VB-B1-GRsch': KeuzelijstWaarde(invulwaarde='VB-B1-GRsch',
                                        label='VB-B1-GRsch',
                                        definitie='Een omgekeerde driehoekmarkering groot en schuin.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCodeVerschuind/VB-B1-GRsch')
    }

