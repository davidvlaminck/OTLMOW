# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHardwareVormfactor(KeuzelijstField):
    """Het soort toestel waarin de fysieke componenten of onderdelen worden vormgegeven."""
    naam = 'KlHardwareVormfactor'
    label = 'Hardware vormfactor'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHardwareVormfactor'
    definition = 'Het soort toestel waarin de fysieke componenten of onderdelen worden vormgegeven.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHardwareVormfactor'
    options = {
        'desktop': KeuzelijstWaarde(invulwaarde='desktop',
                                    label='desktop',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareVormfactor/desktop'),
        'laptop': KeuzelijstWaarde(invulwaarde='laptop',
                                   label='laptop',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareVormfactor/laptop'),
        'server': KeuzelijstWaarde(invulwaarde='server',
                                   label='server',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareVormfactor/server')
    }

