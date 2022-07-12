# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStortsteenType(KeuzelijstField):
    """Stortsteen types."""
    naam = 'KlStortsteenType'
    label = 'Stortsteen type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStortsteenType'
    definition = 'Stortsteen types.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStortsteenType'
    options = {
        'brokken-van-betonpuin': KeuzelijstWaarde(invulwaarde='brokken-van-betonpuin',
                                                  label='brokken van betonpuin',
                                                  status='ingebruik',
                                                  definitie='brokken van betonpuin',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/brokken-van-betonpuin'),
        'brokken-van-breuksteenpuin': KeuzelijstWaarde(invulwaarde='brokken-van-breuksteenpuin',
                                                       label='brokken van breuksteenpuin',
                                                       status='ingebruik',
                                                       definitie='brokken van breuksteenpuin',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/brokken-van-breuksteenpuin'),
        'brokken-van-mengpuin': KeuzelijstWaarde(invulwaarde='brokken-van-mengpuin',
                                                 label='brokken van mengpuin',
                                                 status='ingebruik',
                                                 definitie='brokken van mengpuin',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/brokken-van-mengpuin'),
        'brokken-van-metselwerkpuin': KeuzelijstWaarde(invulwaarde='brokken-van-metselwerkpuin',
                                                       label='brokken van metselwerkpuin',
                                                       status='ingebruik',
                                                       definitie='brokken van metselwerkpuin',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/brokken-van-metselwerkpuin'),
        'dolomiet': KeuzelijstWaarde(invulwaarde='dolomiet',
                                     label='dolomiet',
                                     status='ingebruik',
                                     definitie='dolomiet',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/dolomiet'),
        'kunststeenslag': KeuzelijstWaarde(invulwaarde='kunststeenslag',
                                           label='kunststeenslag',
                                           status='ingebruik',
                                           definitie='brokken van betonpuin',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/kunststeenslag'),
        'natuursteenslag': KeuzelijstWaarde(invulwaarde='natuursteenslag',
                                            label='natuursteenslag',
                                            status='ingebruik',
                                            definitie='natuursteenslag',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/natuursteenslag'),
        'rolgrind': KeuzelijstWaarde(invulwaarde='rolgrind',
                                     label='rolgrind',
                                     status='ingebruik',
                                     definitie='Grind met goed afgeronde korrels.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/rolgrind'),
        'rolsteen': KeuzelijstWaarde(invulwaarde='rolsteen',
                                     label='rolsteen',
                                     status='ingebruik',
                                     definitie='rolsteen',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/rolsteen'),
        'ruwe-breuksteen': KeuzelijstWaarde(invulwaarde='ruwe-breuksteen',
                                            label='ruwe breuksteen',
                                            status='ingebruik',
                                            definitie='een natuursteen van onregelmatige vorm',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/ruwe-breuksteen')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlStortsteenType.get_dummy_data()

