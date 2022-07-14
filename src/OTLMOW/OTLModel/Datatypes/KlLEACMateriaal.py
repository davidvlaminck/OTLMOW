# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACMateriaal(KeuzelijstField):
    """De verschillende materialen voor afschermende constructies."""
    naam = 'KlLEACMateriaal'
    label = 'Materiaal afschermende constructie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACMateriaal'
    definition = 'De verschillende materialen voor afschermende constructies.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACMateriaal'
    options = {
        'geprefabriceerde-beton': KeuzelijstWaarde(invulwaarde='geprefabriceerde-beton',
                                                   label='geprefabriceerde beton',
                                                   status='ingebruik',
                                                   definitie='geleideconstructie bestaande uit geprefabriceerde betonnen elementen',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACMateriaal/geprefabriceerde-beton'),
        'hout-staal': KeuzelijstWaarde(invulwaarde='hout-staal',
                                       label='hout-staal',
                                       status='ingebruik',
                                       definitie='hout-staal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACMateriaal/hout-staal'),
        'in-situ-beton': KeuzelijstWaarde(invulwaarde='in-situ-beton',
                                          label='in situ beton',
                                          status='ingebruik',
                                          definitie='in situ beton',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACMateriaal/in-situ-beton'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='kunststof',
                                      status='ingebruik',
                                      definitie='kunststof',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACMateriaal/kunststof'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  status='ingebruik',
                                  definitie='staal',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACMateriaal/staal')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

