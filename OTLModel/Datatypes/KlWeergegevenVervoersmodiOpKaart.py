# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWeergegevenVervoersmodiOpKaart(KeuzelijstField):
    """De verschillende beschikbare vervoersmodi die op de bijhorende kaart worden meegegeven."""
    naam = 'KlWeergegevenVervoersmodiOpKaart'
    label = 'Weergegeven vervoersmodi op kaart'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeergegevenVervoersmodiOpKaart'
    definition = 'De verschillende beschikbare vervoersmodi die op de bijhorende kaart worden meegegeven.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeergegevenVervoersmodiOpKaart'
    options = {
        'deelauto': KeuzelijstWaarde(invulwaarde='deelauto',
                                     label='Deelauto',
                                     definitie='TODO',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeergegevenVervoersmodiOpKaart/deelauto'),
        'deelfiets': KeuzelijstWaarde(invulwaarde='deelfiets',
                                      label='Deelfiets',
                                      definitie='TODO',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeergegevenVervoersmodiOpKaart/deelfiets'),
        'flexvervoer': KeuzelijstWaarde(invulwaarde='flexvervoer',
                                        label='Flexvervoer',
                                        definitie='TODO',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeergegevenVervoersmodiOpKaart/flexvervoer'),
        'kernnet-aanvullend-net': KeuzelijstWaarde(invulwaarde='kernnet-aanvullend-net',
                                                   label='Kernnet - aanvullend net',
                                                   definitie='TODO',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeergegevenVervoersmodiOpKaart/kernnet-aanvullend-net'),
        'treinnet': KeuzelijstWaarde(invulwaarde='treinnet',
                                     label='Treinnet',
                                     definitie='TODO',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeergegevenVervoersmodiOpKaart/treinnet'),
        'vast-en-semiflex': KeuzelijstWaarde(invulwaarde='vast-en-semiflex',
                                             label='Vast en semiflex',
                                             definitie='TODO',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeergegevenVervoersmodiOpKaart/vast-en-semiflex')
    }

