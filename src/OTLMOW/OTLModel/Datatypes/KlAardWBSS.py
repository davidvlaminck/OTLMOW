# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAardWBSS(KeuzelijstField):
    """De mogelijke vormen die ervoor zorgen dat hemelwater infiltreert langs de waterdoorlatende betonstraatsteen."""
    naam = 'KlAardWBSS'
    label = 'Aard van waterdoorlatende betonstraatsteen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAardWBSS'
    definition = 'De mogelijke vormen die ervoor zorgen dat hemelwater infiltreert langs de waterdoorlatende betonstraatsteen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAardWBSS'
    options = {
        'met-drainageopeningen': KeuzelijstWaarde(invulwaarde='met-drainageopeningen',
                                                  label='met drainageopeningen',
                                                  definitie='Vorm voor waterdoorlatende betonstraatsteen waarbij hemelwater infiltreert langs de betonstraatsteen.',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardWBSS/met-drainageopeningen'),
        'met-verbrede-voegen': KeuzelijstWaarde(invulwaarde='met-verbrede-voegen',
                                                label='met verbrede voegen',
                                                definitie='Vorm voor waterdoorlatende betonstraatsteen waarbij hemelwater infiltreert langs de betonstraatsteen.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardWBSS/met-verbrede-voegen'),
        'poreus-beton': KeuzelijstWaarde(invulwaarde='poreus-beton',
                                         label='poreus beton',
                                         definitie='Vorm voor waterdoorlatende betonstraatsteen waarbij hemelwater infiltreert doorheen de betonstraatsteen.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardWBSS/poreus-beton')
    }

