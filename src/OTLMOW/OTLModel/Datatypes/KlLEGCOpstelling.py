# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCOpstelling(KeuzelijstField):
    """De opstellingen van de geluidswerende constructie."""
    naam = 'KlLEGCOpstelling'
    label = 'Opstelling'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCOpstelling'
    definition = 'De opstellingen van de geluidswerende constructie.'
    deprecated_version = '2.0.0-RC3'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCOpstelling'
    options = {
        'concaaf': KeuzelijstWaarde(invulwaarde='concaaf',
                                    label='concaaf',
                                    definitie='Concave opstelling t.o.v. de weg',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpstelling/concaaf'),
        'schuin-naar-achter-hellend': KeuzelijstWaarde(invulwaarde='schuin-naar-achter-hellend',
                                                       label='schuin naar achter hellend',
                                                       definitie='schuin naar achter hellend t.o.v. de weg',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpstelling/schuin-naar-achter-hellend'),
        'schuin-naar-voor-hellend': KeuzelijstWaarde(invulwaarde='schuin-naar-voor-hellend',
                                                     label='schuin naar voor hellend',
                                                     definitie='schuin naar voor hellend t.o.v. de weg',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpstelling/schuin-naar-voor-hellend'),
        'verticaal': KeuzelijstWaarde(invulwaarde='verticaal',
                                      label='verticaal',
                                      definitie='verticaal t.o.v. de weg',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpstelling/verticaal')
    }

