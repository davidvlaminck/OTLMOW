# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersbordconceptStatus(KeuzelijstField):
    """Keuzelijst met waarden die aangeven of een verkeersbordconcept nog gebruikt wordt."""
    naam = 'KlVerkeersbordconceptStatus'
    label = 'VerkeersbordconceptStatus'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersbordconceptStatus'
    definition = 'Keuzelijst met waarden die aangeven of een verkeersbordconcept nog gebruikt wordt.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersbordconceptStatus'
    options = {
        'afgeschaft': KeuzelijstWaarde(invulwaarde='afgeschaft',
                                       label='afgeschaft',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordconceptStatus/afgeschaft'),
        'stabiel': KeuzelijstWaarde(invulwaarde='stabiel',
                                    label='stabiel',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordconceptStatus/stabiel')
    }

