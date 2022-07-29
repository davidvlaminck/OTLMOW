# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOmegaElementMateriaal(KeuzelijstField):
    """De gebruikte materialen van het omega-element."""
    naam = 'KlOmegaElementMateriaal'
    label = 'Omega element materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOmegaElementMateriaal'
    definition = 'De gebruikte materialen van het omega-element.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOmegaElementMateriaal'
    options = {
        'aluminium': KeuzelijstWaarde(invulwaarde='aluminium',
                                      label='aluminium',
                                      status='ingebruik',
                                      definitie='Omega-element vervaarigd uit aluminium.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmegaElementMateriaal/aluminium'),
        'roestvrij-staal': KeuzelijstWaarde(invulwaarde='roestvrij-staal',
                                            label='roestvrij staal',
                                            status='ingebruik',
                                            definitie='Omega-element vervaarigd uit roestvrij staal.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmegaElementMateriaal/roestvrij-staal'),
        'verzinkt-staal': KeuzelijstWaarde(invulwaarde='verzinkt-staal',
                                           label='verzinkt staal',
                                           status='ingebruik',
                                           definitie='Omega-element vervaarigd uit verzinkt staal.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmegaElementMateriaal/verzinkt-staal')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

