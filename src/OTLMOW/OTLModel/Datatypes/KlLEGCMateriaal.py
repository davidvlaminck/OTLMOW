# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCMateriaal(KeuzelijstField):
    """Materialen van de geluidswerende constructie."""
    naam = 'KlLEGCMateriaal'
    label = 'Materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCMateriaal'
    definition = 'Materialen van de geluidswerende constructie.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCMateriaal'
    options = {
        'bakstenen': KeuzelijstWaarde(invulwaarde='bakstenen',
                                      label='bakstenen',
                                      definitie='bakstenen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/bakstenen'),
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  definitie='beton',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/beton'),
        'beton---houtvezelbeton': KeuzelijstWaarde(invulwaarde='beton---houtvezelbeton',
                                                   label='beton - houtvezelbeton',
                                                   definitie='beton - houtvezelbeton',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/beton---houtvezelbeton'),
        'beton---lichtgewichtbeton': KeuzelijstWaarde(invulwaarde='beton---lichtgewichtbeton',
                                                      label='beton - lichtgewichtbeton',
                                                      definitie='beton - lichtgewichtbeton',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/beton---lichtgewichtbeton'),
        'beton---steenparament': KeuzelijstWaarde(invulwaarde='beton---steenparament',
                                                  label='beton - steenparament',
                                                  definitie='Beton - steenparament',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/beton---steenparament'),
        'glas': KeuzelijstWaarde(invulwaarde='glas',
                                 label='glas',
                                 definitie='glas',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/glas'),
        'groenscherm': KeuzelijstWaarde(invulwaarde='groenscherm',
                                        label='groenscherm',
                                        definitie='groenscherm',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/groenscherm'),
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='hout',
                                 definitie='hout',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/hout'),
        'kokospanelen': KeuzelijstWaarde(invulwaarde='kokospanelen',
                                         label='kokospanelen',
                                         definitie='kokospanelen',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/kokospanelen'),
        'kunststof---PMMA': KeuzelijstWaarde(invulwaarde='kunststof---PMMA',
                                             label='kunststof - PMMA',
                                             definitie='Kunststof - PMMA',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/kunststof---PMMA'),
        'kunststof---PVC': KeuzelijstWaarde(invulwaarde='kunststof---PVC',
                                            label='kunststof - PVC',
                                            definitie='kunststof - PVC',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/kunststof---PVC'),
        'metaal---aluminium': KeuzelijstWaarde(invulwaarde='metaal---aluminium',
                                               label='metaal - aluminium',
                                               definitie='Metaal - aluminium',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/metaal---aluminium'),
        'metaal---aluminium-en-staal': KeuzelijstWaarde(invulwaarde='metaal---aluminium-en-staal',
                                                        label='metaal - aluminium en staal',
                                                        definitie='Metaal - aluminium en staal',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/metaal---aluminium-en-staal'),
        'metaal---staal': KeuzelijstWaarde(invulwaarde='metaal---staal',
                                           label='metaal - staal',
                                           definitie='metaal - staal',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/metaal---staal'),
        'stalen-raster-met-beschermnet-in-kunststof': KeuzelijstWaarde(invulwaarde='stalen-raster-met-beschermnet-in-kunststof',
                                                                       label='stalen raster met beschermnet in kunststof',
                                                                       definitie='stalen raster met beschermnet in kunststof',
                                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/stalen-raster-met-beschermnet-in-kunststof'),
        'tunnelplaat': KeuzelijstWaarde(invulwaarde='tunnelplaat',
                                        label='tunnelplaat',
                                        definitie='tunnelplaat',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCMateriaal/tunnelplaat')
    }

