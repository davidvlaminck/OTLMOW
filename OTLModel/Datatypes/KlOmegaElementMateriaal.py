# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOmegaElementMateriaal(KeuzelijstField):
    """De gebruikte materialen van het omega-element."""
    naam = 'KlOmegaElementMateriaal'
    label = 'Omega element materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOmegaElementMateriaal'
    definition = 'De gebruikte materialen van het omega-element.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOmegaElementMateriaal'
    options = {
        'aluminium': KeuzelijstWaarde(invulwaarde='aluminium',
                                      label='aluminium',
                                      definitie='Omega-element vervaarigd uit aluminium.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmegaElementMateriaal/aluminium'),
        'roestvrij-staal': KeuzelijstWaarde(invulwaarde='roestvrij-staal',
                                            label='roestvrij staal',
                                            definitie='Omega-element vervaarigd uit roestvrij staal.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmegaElementMateriaal/roestvrij-staal'),
        'verzinkt-staal': KeuzelijstWaarde(invulwaarde='verzinkt-staal',
                                           label='verzinkt staal',
                                           definitie='Omega-element vervaarigd uit verzinkt staal.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmegaElementMateriaal/verzinkt-staal')
    }

