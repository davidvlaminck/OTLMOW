# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAansluitstukMateriaal(KeuzelijstField):
    """Het materiaal van het aansluitstuk."""
    naam = 'KlAansluitstukMateriaal'
    label = 'Aansluitstuk materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAansluitstukMateriaal'
    definition = 'Het materiaal van het aansluitstuk.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAansluitstukMateriaal'
    options = {
        'gres': KeuzelijstWaarde(invulwaarde='gres',
                                 label='gres',
                                 definitie='Gres',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitstukMateriaal/gres'),
        'polyethyleen': KeuzelijstWaarde(invulwaarde='polyethyleen',
                                         label='polyethyleen',
                                         definitie='polyethyleen',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitstukMateriaal/polyethyleen'),
        'pp': KeuzelijstWaarde(invulwaarde='pp',
                               label='pp',
                               definitie='Polypropyleen',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitstukMateriaal/pp'),
        'pvc': KeuzelijstWaarde(invulwaarde='pvc',
                                label='pvc',
                                definitie='Polyvinylchloride',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitstukMateriaal/pvc'),
        'pvc-u-composiet': KeuzelijstWaarde(invulwaarde='pvc-u-composiet',
                                            label='pvc-u-composiet',
                                            definitie='pvc-u-composiet',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitstukMateriaal/pvc-u-composiet')
    }

