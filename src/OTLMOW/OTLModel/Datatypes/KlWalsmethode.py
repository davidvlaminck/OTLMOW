# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWalsmethode(KeuzelijstField):
    """De manier waarop het staal is gewalst."""
    naam = 'KlWalsmethode'
    label = 'Walsmethode'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlWalsmethode'
    definition = 'De manier waarop het staal is gewalst.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWalsmethode'
    options = {
        'koud': KeuzelijstWaarde(invulwaarde='koud',
                                 label='Koud',
                                 definitie='Staal die bij omgevingstemperatuur wordt gevormd (getrokken) uit warmgewalst staal.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWalsmethode/koud'),
        'warm': KeuzelijstWaarde(invulwaarde='warm',
                                 label='Warm',
                                 definitie='Heet staal wordt vervormd onder druk van persen en walsen.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWalsmethode/warm')
    }

