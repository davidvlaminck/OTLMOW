# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDetectiecameraDetectieprincipe(KeuzelijstField):
    """Keuzelijst met detectieprincipes voor Detectiecamera."""
    naam = 'KlDetectiecameraDetectieprincipe'
    label = 'Detectiecamera detectieprincipe'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDetectiecameraDetectieprincipe'
    definition = 'Keuzelijst met detectieprincipes voor Detectiecamera.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDetectiecameraDetectieprincipe'
    options = {
        'optisch': KeuzelijstWaarde(invulwaarde='optisch',
                                    label='optisch',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectiecameraDetectieprincipe/optisch'),
        'thermografisch': KeuzelijstWaarde(invulwaarde='thermografisch',
                                           label='thermografisch',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectiecameraDetectieprincipe/thermografisch')
    }

