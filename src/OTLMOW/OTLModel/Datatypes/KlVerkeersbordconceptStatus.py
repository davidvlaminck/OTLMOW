# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersbordconceptStatus(KeuzelijstField):
    """Keuzelijst met waarden die aangeven of een verkeersbordconcept nog gebruikt wordt."""
    naam = 'KlVerkeersbordconceptStatus'
    label = 'VerkeersbordconceptStatus'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersbordconceptStatus'
    definition = 'Keuzelijst met waarden die aangeven of een verkeersbordconcept nog gebruikt wordt.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersbordconceptStatus'
    options = {
        'afgeschaft': KeuzelijstWaarde(invulwaarde='afgeschaft',
                                       label='afgeschaft',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordconceptStatus/afgeschaft'),
        'stabiel': KeuzelijstWaarde(invulwaarde='stabiel',
                                    label='stabiel',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordconceptStatus/stabiel')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

