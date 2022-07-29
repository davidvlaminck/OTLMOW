# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgRijrichting(KeuzelijstField):
    """De mogelijke rijrichtingen."""
    naam = 'KlAlgRijrichting'
    label = 'Rijrichting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAlgRijrichting'
    definition = 'De mogelijke rijrichtingen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgRijrichting'
    options = {
        'aflopend': KeuzelijstWaarde(invulwaarde='aflopend',
                                     label='aflopend',
                                     status='ingebruik',
                                     definitie='Aflopende rijrichting.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgRijrichting/aflopend'),
        'oplopend': KeuzelijstWaarde(invulwaarde='oplopend',
                                     label='oplopend',
                                     status='ingebruik',
                                     definitie='Oplopende rijrichting.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgRijrichting/oplopend')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

