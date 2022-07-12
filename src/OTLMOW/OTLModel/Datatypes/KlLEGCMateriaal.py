# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCMateriaal(KeuzelijstField):
    """Materialen van de geluidswerende constructie."""
    naam = 'KlLEGCMateriaal'
    label = 'Materiaal geluidswerende constructie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCMateriaal'
    definition = 'Materialen van de geluidswerende constructie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCMateriaal'
    options = {
        'bakstenen': KeuzelijstWaarde(invulwaarde='bakstenen',
                                      label='bakstenen',
                                      status='ingebruik',
                                      definitie='bakstenen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/bakstenen'),
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='ingebruik',
                                  definitie='beton',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/beton'),
        'beton---houtvezelbeton': KeuzelijstWaarde(invulwaarde='beton---houtvezelbeton',
                                                   label='beton - houtvezelbeton',
                                                   status='ingebruik',
                                                   definitie='beton - houtvezelbeton',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/beton---houtvezelbeton'),
        'beton---lichtgewichtbeton': KeuzelijstWaarde(invulwaarde='beton---lichtgewichtbeton',
                                                      label='beton - lichtgewichtbeton',
                                                      status='ingebruik',
                                                      definitie='beton - lichtgewichtbeton',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/beton---lichtgewichtbeton'),
        'beton---steenparament': KeuzelijstWaarde(invulwaarde='beton---steenparament',
                                                  label='beton - steenparament',
                                                  status='ingebruik',
                                                  definitie='Beton - steenparament',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/beton---steenparament'),
        'glas': KeuzelijstWaarde(invulwaarde='glas',
                                 label='glas',
                                 status='ingebruik',
                                 definitie='glas',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/glas'),
        'groenscherm': KeuzelijstWaarde(invulwaarde='groenscherm',
                                        label='groenscherm',
                                        status='ingebruik',
                                        definitie='groenscherm',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/groenscherm'),
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='hout',
                                 status='ingebruik',
                                 definitie='hout',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/hout'),
        'kokospanelen': KeuzelijstWaarde(invulwaarde='kokospanelen',
                                         label='kokospanelen',
                                         status='ingebruik',
                                         definitie='kokospanelen',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/kokospanelen'),
        'kunststof---PMMA': KeuzelijstWaarde(invulwaarde='kunststof---PMMA',
                                             label='kunststof - PMMA',
                                             status='ingebruik',
                                             definitie='Kunststof - PMMA',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/kunststof---PMMA'),
        'kunststof---PVC': KeuzelijstWaarde(invulwaarde='kunststof---PVC',
                                            label='kunststof - PVC',
                                            status='ingebruik',
                                            definitie='kunststof - PVC',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/kunststof---PVC'),
        'metaal---aluminium': KeuzelijstWaarde(invulwaarde='metaal---aluminium',
                                               label='metaal - aluminium',
                                               status='ingebruik',
                                               definitie='Metaal - aluminium',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/metaal---aluminium'),
        'metaal---aluminium-en-staal': KeuzelijstWaarde(invulwaarde='metaal---aluminium-en-staal',
                                                        label='metaal - aluminium en staal',
                                                        status='ingebruik',
                                                        definitie='Metaal - aluminium en staal',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/metaal---aluminium-en-staal'),
        'metaal---staal': KeuzelijstWaarde(invulwaarde='metaal---staal',
                                           label='metaal - staal',
                                           status='ingebruik',
                                           definitie='metaal - staal',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/metaal---staal'),
        'stalen-raster-met-beschermnet-in-kunststof': KeuzelijstWaarde(invulwaarde='stalen-raster-met-beschermnet-in-kunststof',
                                                                       label='stalen raster met beschermnet in kunststof',
                                                                       status='ingebruik',
                                                                       definitie='stalen raster met beschermnet in kunststof',
                                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/stalen-raster-met-beschermnet-in-kunststof'),
        'tunnelplaat': KeuzelijstWaarde(invulwaarde='tunnelplaat',
                                        label='tunnelplaat',
                                        status='ingebruik',
                                        definitie='tunnelplaat',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/tunnelplaat')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlLEGCMateriaal.get_dummy_data()

