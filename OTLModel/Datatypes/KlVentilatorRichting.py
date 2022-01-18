# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVentilatorRichting(KeuzelijstField):
    """Keuzelijst die aangeeft of de luchtstroom in één richting of beide richtingen kan plaatsvinden."""
    naam = 'KlVentilatorRichting'
    label = 'Ventilator richting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVentilatorRichting'
    definition = 'Keuzelijst die aangeeft of de luchtstroom in één richting of beide richtingen kan plaatsvinden.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVentilatorRichting'
    options = {
        'bidirectioneel': KeuzelijstWaarde(invulwaarde='bidirectioneel',
                                           label='bidirectioneel',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorRichting/bidirectioneel'),
        'unidirectioneel': KeuzelijstWaarde(invulwaarde='unidirectioneel',
                                            label='unidirectioneel',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorRichting/unidirectioneel')
    }

