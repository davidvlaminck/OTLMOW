# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEMDraagconstructieElekBeveiliging(KeuzelijstField):
    """Type elektrische beveiliging aanwezig in de draagconstructie."""
    naam = 'KlEMDraagconstructieElekBeveiliging'
    label = 'EM-draagconstructie elektrische beveiliging'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlEMDraagconstructieElekBeveiliging'
    definition = 'Type elektrische beveiliging aanwezig in de draagconstructie.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEMDraagconstructieElekBeveiliging'
    options = {
        'automaat': KeuzelijstWaarde(invulwaarde='automaat',
                                     label='automaat',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEMDraagconstructieElekBeveiliging/automaat'),
        'differentieelautomaat': KeuzelijstWaarde(invulwaarde='differentieelautomaat',
                                                  label='differentieelautomaat',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEMDraagconstructieElekBeveiliging/differentieelautomaat'),
        'smeltzekering': KeuzelijstWaarde(invulwaarde='smeltzekering',
                                          label='smeltzekering',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEMDraagconstructieElekBeveiliging/smeltzekering')
    }

