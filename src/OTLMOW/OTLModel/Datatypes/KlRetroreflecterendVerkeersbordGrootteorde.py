# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRetroreflecterendVerkeersbordGrootteorde(KeuzelijstField):
    """Opties om de grootteorde van een RetroreflecterendVerkeersbord aan te geven zoals gedefinieerd in SB250."""
    naam = 'KlRetroreflecterendVerkeersbordGrootteorde'
    label = 'Retroreflecterend verkeersbord grootteorde'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRetroreflecterendVerkeersbordGrootteorde'
    definition = 'Opties om de grootteorde van een RetroreflecterendVerkeersbord aan te geven zoals gedefinieerd in SB250.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRetroreflecterendVerkeersbordGrootteorde'
    options = {
        'groot': KeuzelijstWaarde(invulwaarde='groot',
                                  label='groot',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRetroreflecterendVerkeersbordGrootteorde/groot'),
        'klein': KeuzelijstWaarde(invulwaarde='klein',
                                  label='klein',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRetroreflecterendVerkeersbordGrootteorde/klein'),
        'middelgroot': KeuzelijstWaarde(invulwaarde='middelgroot',
                                        label='middelgroot',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRetroreflecterendVerkeersbordGrootteorde/middelgroot')
    }

