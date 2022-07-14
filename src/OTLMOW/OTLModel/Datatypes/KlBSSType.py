# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBSSType(KeuzelijstField):
    """Types van betonstraatsteen en betontegel."""
    naam = 'KlBSSType'
    label = 'BSS type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBSSType'
    definition = 'Types van betonstraatsteen en betontegel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBSSType'
    options = {
        'gekleurde-met-anorganische-pigmenten': KeuzelijstWaarde(invulwaarde='gekleurde-met-anorganische-pigmenten',
                                                                 label='gekleurde met anorganische pigmenten',
                                                                 status='ingebruik',
                                                                 definitie='Gekleurde betonstraatstenen met anorganische pigmenten.',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBSSType/gekleurde-met-anorganische-pigmenten'),
        'gekleurde-met-kleurondersteunende-granulaten': KeuzelijstWaarde(invulwaarde='gekleurde-met-kleurondersteunende-granulaten',
                                                                         label='gekleurde met kleurondersteunende granulaten',
                                                                         status='ingebruik',
                                                                         definitie='Gekleurde betonstraatstenen met kleurondersteunende granulaten.',
                                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBSSType/gekleurde-met-kleurondersteunende-granulaten'),
        'grijze': KeuzelijstWaarde(invulwaarde='grijze',
                                   label='grijze',
                                   status='ingebruik',
                                   definitie='Grijze betonstraatstenen.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBSSType/grijze'),
        'witte-met-kleurondersteunende-granulaten': KeuzelijstWaarde(invulwaarde='witte-met-kleurondersteunende-granulaten',
                                                                     label='witte met kleurondersteunende granulaten',
                                                                     status='ingebruik',
                                                                     definitie='Witte betonstraatstenen met kleurondersteunende granulaten.',
                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBSSType/witte-met-kleurondersteunende-granulaten')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

