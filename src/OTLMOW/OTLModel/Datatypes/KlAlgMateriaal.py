# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgMateriaal(KeuzelijstField):
    """Het materiaal waaruit een object voornamelijk gebouwd is."""
    naam = 'KlAlgMateriaal'
    label = 'Materiaal soorten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAlgMateriaal'
    definition = 'Het materiaal waaruit een object voornamelijk gebouwd is.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgMateriaal'
    options = {
        'aluminium': KeuzelijstWaarde(invulwaarde='aluminium',
                                      label='aluminium',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/aluminium'),
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/beton'),
        'glasvezelversterkt-polyester': KeuzelijstWaarde(invulwaarde='glasvezelversterkt-polyester',
                                                         label='glasvezelversterkt polyester',
                                                         status='ingebruik',
                                                         definitie='glasvezelversterkt polyester',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/glasvezelversterkt-polyester'),
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='hout',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/hout'),
        'houtvezelbeton': KeuzelijstWaarde(invulwaarde='houtvezelbeton',
                                           label='houtvezelbeton',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/houtvezelbeton'),
        'kunstof': KeuzelijstWaarde(invulwaarde='kunstof',
                                    label='kunstof',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/kunstof'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='kunststof',
                                      status='ingebruik',
                                      definitie='kunststof',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/kunststof'),
        'metselwerk': KeuzelijstWaarde(invulwaarde='metselwerk',
                                       label='metselwerk',
                                       status='ingebruik',
                                       definitie='metselwerk',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/metselwerk'),
        'polycarbonaat': KeuzelijstWaarde(invulwaarde='polycarbonaat',
                                          label='polycarbonaat',
                                          status='ingebruik',
                                          definitie='polycarbonaat',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/polycarbonaat'),
        'roestvrijstaal': KeuzelijstWaarde(invulwaarde='roestvrijstaal',
                                           label='roestvrijstaal',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/roestvrijstaal'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  status='ingebruik',
                                  definitie='staal',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/staal')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

