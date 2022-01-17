# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHuisaansluitputMateriaal(KeuzelijstField):
    """Materialen voor een huisaansluitput."""
    naam = 'KlHuisaansluitputMateriaal'
    label = 'Huisaansluitput materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHuisaansluitputMateriaal'
    definition = 'Materialen voor een huisaansluitput.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHuisaansluitputMateriaal'
    options = {
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  definitie='betonnen huisaansluitputje',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHuisaansluitputMateriaal/beton'),
        'gres': KeuzelijstWaarde(invulwaarde='gres',
                                 label='gres',
                                 definitie='aansluitputje in grès',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHuisaansluitputMateriaal/gres'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='kunststof',
                                      definitie='kunstof aansluitputje',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHuisaansluitputMateriaal/kunststof')
    }

