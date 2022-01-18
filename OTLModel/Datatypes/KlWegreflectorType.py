# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWegreflectorType(KeuzelijstField):
    """De vormen van een wegreflector."""
    naam = 'KlWegreflectorType'
    label = 'Wegreflector type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWegreflectorType'
    definition = 'De vormen van een wegreflector.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWegreflectorType'
    options = {
        'glasbolreflector-100-mm-diameter': KeuzelijstWaarde(invulwaarde='glasbolreflector-100-mm-diameter',
                                                             label='glasbolreflector 100 mm diameter',
                                                             definitie='Een wegreflector in glas en diameter 100 millimeter met als doel de geleiding van de weggebruiker langs de weg',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegreflectorType/glasbolreflector-100-mm-diameter'),
        'glasbolreflector-50-mm-diameter': KeuzelijstWaarde(invulwaarde='glasbolreflector-50-mm-diameter',
                                                            label='glasbolreflector 50 mm diameter',
                                                            definitie='Een wegreflector in glas en diameter 50 millimeter met als doel de geleiding van de weggebruiker langs de weg',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegreflectorType/glasbolreflector-50-mm-diameter'),
        'kunststof-wegdekreflector': KeuzelijstWaarde(invulwaarde='kunststof-wegdekreflector',
                                                      label='kunststof wegdekreflector',
                                                      definitie='Een kunststoffen wegreflector aangebracht op de rijbaan met als doel de zichtbaarheid van verkeerseilanden te verhogen en geleiding van de weggebruiker langs de weg',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegreflectorType/kunststof-wegdekreflector'),
        'metalen-wegdekreflector': KeuzelijstWaarde(invulwaarde='metalen-wegdekreflector',
                                                    label='metalen wegdekreflector',
                                                    definitie='Een metalen wegreflector aangebracht op de rijbaan met als doel de zichtbaarheid van verkeerseilanden te verhogen en geleiding van de weggebruiker langs de weg',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegreflectorType/metalen-wegdekreflector')
    }

