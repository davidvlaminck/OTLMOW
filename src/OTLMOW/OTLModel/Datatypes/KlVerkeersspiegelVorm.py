# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersspiegelVorm(KeuzelijstField):
    """De vormen van een verkeersspiegel."""
    naam = 'KlVerkeersspiegelVorm'
    label = 'Verkeersspiegel vorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersspiegelVorm'
    definition = 'De vormen van een verkeersspiegel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersspiegelVorm'
    options = {
        'rechthoekig': KeuzelijstWaarde(invulwaarde='rechthoekig',
                                        label='rechthoekig',
                                        status='ingebruik',
                                        definitie='rechthoekige verkeersspiegel',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersspiegelVorm/rechthoekig'),
        'rond': KeuzelijstWaarde(invulwaarde='rond',
                                 label='rond',
                                 status='ingebruik',
                                 definitie='ronde verkeersspiegel',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersspiegelVorm/rond')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

