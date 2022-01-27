# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDivergentiepuntbebakeningselementType(KeuzelijstField):
    """De vormen van het divergentiepuntbebakeningselement."""
    naam = 'KlDivergentiepuntbebakeningselementType'
    label = 'Divergentiepuntbebakeningselementtype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDivergentiepuntbebakeningselementType'
    definition = 'De vormen van het divergentiepuntbebakeningselement.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDivergentiepuntbebakeningselementType'
    options = {
        'klein-model': KeuzelijstWaarde(invulwaarde='klein-model',
                                        label='klein model',
                                        definitie='Divergentiepuntbebakeningselement van 1 meter diameter (folie type 3.a).',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDivergentiepuntbebakeningselementType/klein-model'),
        'standaard-model': KeuzelijstWaarde(invulwaarde='standaard-model',
                                            label='standaard model',
                                            definitie='Divergentiepuntbebakeningselement van 2 meter diameter (folie type 2).',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDivergentiepuntbebakeningselementType/standaard-model')
    }

