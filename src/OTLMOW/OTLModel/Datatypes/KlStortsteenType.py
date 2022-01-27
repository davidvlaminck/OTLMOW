# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStortsteenType(KeuzelijstField):
    """Stortsteen types."""
    naam = 'KlStortsteenType'
    label = 'Stortsteen type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStortsteenType'
    definition = 'Stortsteen types.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStortsteenType'
    options = {
        'brokken-van-betonpuin': KeuzelijstWaarde(invulwaarde='brokken-van-betonpuin',
                                                  label='brokken van betonpuin',
                                                  definitie='brokken van betonpuin',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/brokken-van-betonpuin'),
        'brokken-van-breuksteenpuin': KeuzelijstWaarde(invulwaarde='brokken-van-breuksteenpuin',
                                                       label='brokken van breuksteenpuin',
                                                       definitie='brokken van breuksteenpuin',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/brokken-van-breuksteenpuin'),
        'brokken-van-mengpuin': KeuzelijstWaarde(invulwaarde='brokken-van-mengpuin',
                                                 label='brokken van mengpuin',
                                                 definitie='brokken van mengpuin',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/brokken-van-mengpuin'),
        'brokken-van-metselwerkpuin': KeuzelijstWaarde(invulwaarde='brokken-van-metselwerkpuin',
                                                       label='brokken van metselwerkpuin',
                                                       definitie='brokken van metselwerkpuin',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/brokken-van-metselwerkpuin'),
        'dolomiet': KeuzelijstWaarde(invulwaarde='dolomiet',
                                     label='dolomiet',
                                     definitie='dolomiet',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/dolomiet'),
        'kunststeenslag': KeuzelijstWaarde(invulwaarde='kunststeenslag',
                                           label='kunststeenslag',
                                           definitie='brokken van betonpuin',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/kunststeenslag'),
        'natuursteenslag': KeuzelijstWaarde(invulwaarde='natuursteenslag',
                                            label='natuursteenslag',
                                            definitie='natuursteenslag',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/natuursteenslag'),
        'rolgrind': KeuzelijstWaarde(invulwaarde='rolgrind',
                                     label='rolgrind',
                                     definitie='Grind met goed afgeronde korrels.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/rolgrind'),
        'rolsteen': KeuzelijstWaarde(invulwaarde='rolsteen',
                                     label='rolsteen',
                                     definitie='rolsteen',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/rolsteen'),
        'ruwe-breuksteen': KeuzelijstWaarde(invulwaarde='ruwe-breuksteen',
                                            label='ruwe breuksteen',
                                            definitie='een natuursteen van onregelmatige vorm',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/ruwe-breuksteen')
    }

