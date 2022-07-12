# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWBSSType(KeuzelijstField):
    """Types van waterdoorlatende betonstraatstenen en betontegels."""
    naam = 'KlWBSSType'
    label = 'WBSS type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWBSSType'
    definition = 'Types van waterdoorlatende betonstraatstenen en betontegels.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWBSSType'
    options = {
        'gekleurde-met-anorganische-pigmenten': KeuzelijstWaarde(invulwaarde='gekleurde-met-anorganische-pigmenten',
                                                                 label='gekleurde met anorganische pigmenten',
                                                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                 definitie='gekleurde waterdoorlatende betonstraatstenen met anorganische pigmenten',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWBSSType/gekleurde-met-anorganische-pigmenten'),
        'gekleurde-met-kleurondersteunende-granulaten': KeuzelijstWaarde(invulwaarde='gekleurde-met-kleurondersteunende-granulaten',
                                                                         label='gekleurde met kleurondersteunende granulaten',
                                                                         status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                         definitie='gekleurde waterdoorlatende betonstraatstenen met kleurondersteunende granulaten',
                                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWBSSType/gekleurde-met-kleurondersteunende-granulaten'),
        'grijze': KeuzelijstWaarde(invulwaarde='grijze',
                                   label='grijze',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='grijze waterdoorlatende betonstraatstenen',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWBSSType/grijze'),
        'waterdoorlatende-betontegel': KeuzelijstWaarde(invulwaarde='waterdoorlatende-betontegel',
                                                        label='waterdoorlatende betontegel',
                                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                        definitie='waterdoorlatende betontegel',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWBSSType/waterdoorlatende-betontegel'),
        'witte-met-kleurondersteunende-granulaten': KeuzelijstWaarde(invulwaarde='witte-met-kleurondersteunende-granulaten',
                                                                     label='witte met kleurondersteunende granulaten',
                                                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                     definitie='witte waterdoorlatende betonstraatstenen met kleurondersteunende granulaten',
                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWBSSType/witte-met-kleurondersteunende-granulaten')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlWBSSType.get_dummy_data()

