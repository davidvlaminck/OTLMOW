# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEcoEcokokerType(KeuzelijstField):
    """Types van ecokoker."""
    naam = 'KlEcoEcokokerType'
    label = 'Ecokoker type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEcoEcokokerType'
    definition = 'Types van ecokoker.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEcoEcokokerType'
    options = {
        'amfibieenkoker': KeuzelijstWaarde(invulwaarde='amfibieenkoker',
                                           label='amfibieenkoker',
                                           definitie='Een ecokoker voor amfibieën.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoEcokokerType/amfibieenkoker'),
        'betonnen-ecokoker': KeuzelijstWaarde(invulwaarde='betonnen-ecokoker',
                                              label='betonnen ecokoker',
                                              definitie='Een ecokoker uit beton.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoEcokokerType/betonnen-ecokoker')
    }

