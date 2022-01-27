# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDraagConstrBijzondertransport(KeuzelijstField):
    """De mogelijkheden en manieren waarop een steun geschikt is om bijzonder transport mogelijk te maken."""
    naam = 'KlDraagConstrBijzondertransport'
    label = 'Draagconstructie bijzonder transport'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlDraagConstrBijzondertransport'
    definition = 'De mogelijkheden en manieren waarop een steun geschikt is om bijzonder transport mogelijk te maken.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDraagConstrBijzondertransport'
    options = {
        'afkoppelbaar': KeuzelijstWaarde(invulwaarde='afkoppelbaar',
                                         label='afkoppelbaar',
                                         definitie='Het object is afkoppelbaar.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagConstrBijzondertransport/afkoppelbaar'),
        'draaibaar': KeuzelijstWaarde(invulwaarde='draaibaar',
                                      label='draaibaar',
                                      definitie='Het object is draaibaar.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagConstrBijzondertransport/draaibaar'),
        'geen-voorziening': KeuzelijstWaarde(invulwaarde='geen-voorziening',
                                             label='geen voorziening',
                                             definitie='Geen voorziening.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagConstrBijzondertransport/geen-voorziening'),
        'kantelbaar': KeuzelijstWaarde(invulwaarde='kantelbaar',
                                       label='kantelbaar',
                                       definitie='Het object is kantelbaar.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagConstrBijzondertransport/kantelbaar')
    }

