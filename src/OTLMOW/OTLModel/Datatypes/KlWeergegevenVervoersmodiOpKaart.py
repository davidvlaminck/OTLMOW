# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWeergegevenVervoersmodiOpKaart(KeuzelijstField):
    """De verschillende beschikbare vervoersmodi die op de bijhorende kaart worden meegegeven."""
    naam = 'KlWeergegevenVervoersmodiOpKaart'
    label = 'Weergegeven vervoersmodi op kaart'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeergegevenVervoersmodiOpKaart'
    definition = 'De verschillende beschikbare vervoersmodi die op de bijhorende kaart worden meegegeven.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeergegevenVervoersmodiOpKaart'
    options = {
        'deelauto': KeuzelijstWaarde(invulwaarde='deelauto',
                                     label='Deelauto',
                                     status='ingebruik',
                                     definitie='TODO',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeergegevenVervoersmodiOpKaart/deelauto'),
        'deelfiets': KeuzelijstWaarde(invulwaarde='deelfiets',
                                      label='Deelfiets',
                                      status='ingebruik',
                                      definitie='TODO',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeergegevenVervoersmodiOpKaart/deelfiets'),
        'flexvervoer': KeuzelijstWaarde(invulwaarde='flexvervoer',
                                        label='Flexvervoer',
                                        status='ingebruik',
                                        definitie='TODO',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeergegevenVervoersmodiOpKaart/flexvervoer'),
        'kernnet-aanvullend-net': KeuzelijstWaarde(invulwaarde='kernnet-aanvullend-net',
                                                   label='Kernnet - aanvullend net',
                                                   status='ingebruik',
                                                   definitie='TODO',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeergegevenVervoersmodiOpKaart/kernnet-aanvullend-net'),
        'treinnet': KeuzelijstWaarde(invulwaarde='treinnet',
                                     label='Treinnet',
                                     status='ingebruik',
                                     definitie='TODO',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeergegevenVervoersmodiOpKaart/treinnet'),
        'vast-en-semiflex': KeuzelijstWaarde(invulwaarde='vast-en-semiflex',
                                             label='Vast en semiflex',
                                             status='ingebruik',
                                             definitie='TODO',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeergegevenVervoersmodiOpKaart/vast-en-semiflex')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

