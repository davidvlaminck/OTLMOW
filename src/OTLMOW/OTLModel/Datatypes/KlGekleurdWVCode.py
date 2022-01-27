# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGekleurdWVCode(KeuzelijstField):
    """Codes voor een gekleurd wegvlak."""
    naam = 'KlGekleurdWVCode'
    label = 'Gekleurd WV code'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGekleurdWVCode'
    definition = 'Codes voor een gekleurd wegvlak.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGekleurdWVCode'
    options = {
        'GW-FOP': KeuzelijstWaarde(invulwaarde='GW-FOP',
                                   label='GW-FOP',
                                   definitie='Gekleurd wegvlak voor fietsoversteekplaats met blokken.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-FOP'),
        'GW-FP': KeuzelijstWaarde(invulwaarde='GW-FP',
                                  label='GW-FP',
                                  definitie='Gekleurd wegvlak voor fietsoversteekplaats met lijnen.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-FP'),
        'GW-FSUG': KeuzelijstWaarde(invulwaarde='GW-FSUG',
                                    label='GW-FSUG',
                                    definitie='Gekleurd wegvlak voor fietssuggestiestrook (oker,grijs).',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-FSUG'),
        'GW-FSUG-A': KeuzelijstWaarde(invulwaarde='GW-FSUG-A',
                                      label='GW-FSUG-A',
                                      definitie='Gekleurd wegvlak voor fietssuggestiestrook (groen,geel,rood).',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-FSUG-A'),
        'GW-MID': KeuzelijstWaarde(invulwaarde='GW-MID',
                                   label='GW-MID',
                                   definitie='Gekleurd wegvlak voor middengeleider(bv.groene strook)',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-MID'),
        'GW-MV': KeuzelijstWaarde(invulwaarde='GW-MV',
                                  label='GW-MV',
                                  definitie='Gekleurd wegvlak voor parkeerplaats mindervaliden.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-MV'),
        'GW-OFOS': KeuzelijstWaarde(invulwaarde='GW-OFOS',
                                    label='GW-OFOS',
                                    definitie='Gekleurd wegvlak voor voor OFOS.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-OFOS'),
        'GW-OFOS-VAR': KeuzelijstWaarde(invulwaarde='GW-OFOS-VAR',
                                        label='GW-OFOS-VAR',
                                        definitie='Gekleurd wegvlak voor OFOS variant.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-OFOS-VAR'),
        'GW-PLAT': KeuzelijstWaarde(invulwaarde='GW-PLAT',
                                    label='GW-PLAT',
                                    definitie='Gekleurd wegvlak voor verkeersplateau.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-PLAT'),
        'GW-VOP': KeuzelijstWaarde(invulwaarde='GW-VOP',
                                   label='GW-VOP',
                                   definitie='Gekleurd wegvlak voor voetgangers-oversteekplaats.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-VOP')
    }

