# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMasttypePunctueleVerlichting(KeuzelijstField):
    """Het type van de mast voor punctuele verlichting."""
    naam = 'KlMasttypePunctueleVerlichting'
    label = 'Masttype voor punctuele verlichting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMasttypePunctueleVerlichting'
    definition = 'Het type van de mast voor punctuele verlichting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMasttypePunctueleVerlichting'
    options = {
        'mt': KeuzelijstWaarde(invulwaarde='mt',
                               label='MT',
                               status='ingebruik',
                               definitie='Metalen galgmast voor punctuele verlichting met inplantingsstuk.',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMasttypePunctueleVerlichting/mt'),
        'mts': KeuzelijstWaarde(invulwaarde='mts',
                                label='MTS',
                                status='ingebruik',
                                definitie='Metalen galgmast voor punctuele verlichting op voetplaat.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMasttypePunctueleVerlichting/mts')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

