# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMasttypePunctueleVerlichting(KeuzelijstField):
    """Het type van de mast voor punctuele verlichting."""
    naam = 'KlMasttypePunctueleVerlichting'
    label = 'Masttype voor punctuele verlichting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMasttypePunctueleVerlichting'
    definition = 'Het type van de mast voor punctuele verlichting.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMasttypePunctueleVerlichting'
    options = {
        'MT': KeuzelijstWaarde(invulwaarde='MT',
                                      label='MT',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMasttypePunctueleVerlichting/MT'),
        'MTS': KeuzelijstWaarde(invulwaarde='MTS',
                                  label='MTS',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMasttypePunctueleVerlichting/MTS')
    }

