# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACMateriaal(KeuzelijstField):
    """De verschillende materialen voor afschermende constructies."""
    naam = 'KlLEACMateriaal'
    label = 'Materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACMateriaal'
    definition = 'De verschillende materialen voor afschermende constructies.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACMateriaal'
    options = {
        'geprefabriceerde-beton': KeuzelijstWaarde(invulwaarde='geprefabriceerde-beton',
                                                   label='geprefabriceerde beton',
                                                   definitie='geleideconstructie bestaande uit geprefabriceerde betonnen elementen',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACMateriaal/geprefabriceerde-beton'),
        'hout-staal': KeuzelijstWaarde(invulwaarde='hout-staal',
                                       label='hout-staal',
                                       definitie='hout-staal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACMateriaal/hout-staal'),
        'in-situ-beton': KeuzelijstWaarde(invulwaarde='in-situ-beton',
                                          label='in situ beton',
                                          definitie='in situ beton',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACMateriaal/in-situ-beton'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='kunststof',
                                      definitie='kunststof',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACMateriaal/kunststof'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  definitie='staal',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACMateriaal/staal')
    }

