# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWildreflectorDrager(KeuzelijstField):
    """Mogelijke dragers van een wildreflector."""
    naam = 'KlWildreflectorDrager'
    label = 'Wildreflector drager'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWildreflectorDrager'
    definition = 'Mogelijke dragers van een wildreflector.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWildreflectorDrager'
    options = {
        'houten-paal': KeuzelijstWaarde(invulwaarde='houten-paal',
                                        label='houten paal',
                                        definitie='houten paal als drager.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWildreflectorDrager/houten-paal'),
        'metalen-paal': KeuzelijstWaarde(invulwaarde='metalen-paal',
                                         label='metalen paal',
                                         definitie='metalen paal als drager.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWildreflectorDrager/metalen-paal')
    }

