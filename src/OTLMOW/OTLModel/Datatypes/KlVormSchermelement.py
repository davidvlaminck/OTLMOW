# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVormSchermelement(KeuzelijstField):
    """Deze keuzelijst geeft aan of het schermelement recht of gebogen is."""
    naam = 'KlVormSchermelement'
    label = 'Vorm schermelement'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVormSchermelement'
    definition = 'Deze keuzelijst geeft aan of het schermelement recht of gebogen is.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVormSchermelement'
    options = {
        'gebogen': KeuzelijstWaarde(invulwaarde='gebogen',
                                    label='gebogen',
                                    definitie='gebogen',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormSchermelement/gebogen'),
        'recht': KeuzelijstWaarde(invulwaarde='recht',
                                  label='recht',
                                  definitie='recht',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormSchermelement/recht')
    }

