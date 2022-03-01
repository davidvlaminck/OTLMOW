# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgMateriaal(KeuzelijstField):
    """Het materiaal waaruit een object voornamelijk gebouwd is."""
    naam = 'KlAlgMateriaal'
    label = 'Materiaal soorten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAlgMateriaal'
    definition = 'Het materiaal waaruit een object voornamelijk gebouwd is.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgMateriaal'
    options = {
        'aluminium': KeuzelijstWaarde(invulwaarde='aluminium',
                                      label='aluminium',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/aluminium'),
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/beton'),
        'glasvezelversterkt-polyester': KeuzelijstWaarde(invulwaarde='glasvezelversterkt-polyester',
                                                         label='glasvezelversterkt polyester',
                                                         definitie='glasvezelversterkt polyester',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/glasvezelversterkt-polyester'),
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='hout',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/hout'),
        'houtvezelbeton': KeuzelijstWaarde(invulwaarde='houtvezelbeton',
                                           label='houtvezelbeton',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/houtvezelbeton'),
        'kunstof': KeuzelijstWaarde(invulwaarde='kunstof',
                                    label='kunstof',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/kunstof'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='kunststof',
                                      definitie='kunststof',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/kunststof'),
        'metselwerk': KeuzelijstWaarde(invulwaarde='metselwerk',
                                       label='metselwerk',
                                       definitie='metselwerk',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/metselwerk'),
        'polycarbonaat': KeuzelijstWaarde(invulwaarde='polycarbonaat',
                                          label='polycarbonaat',
                                          definitie='polycarbonaat',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/polycarbonaat'),
        'roestvrijstaal': KeuzelijstWaarde(invulwaarde='roestvrijstaal',
                                           label='roestvrijstaal',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/roestvrijstaal'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  definitie='staal',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/staal')
    }

