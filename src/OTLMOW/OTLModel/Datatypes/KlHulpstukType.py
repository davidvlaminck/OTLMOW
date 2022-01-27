# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHulpstukType(KeuzelijstField):
    """Het type van het hulpstuk."""
    naam = 'KlHulpstukType'
    label = 'Hulpstuk type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHulpstukType'
    definition = 'Het type van het hulpstuk.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHulpstukType'
    options = {
        'T-stuk': KeuzelijstWaarde(invulwaarde='T-stuk',
                                   label='T-stuk',
                                   definitie='T-stuk',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulpstukType/T-stuk'),
        'Y-stuk': KeuzelijstWaarde(invulwaarde='Y-stuk',
                                   label='Y-stuk',
                                   definitie='Y-stuk',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulpstukType/Y-stuk'),
        'aansluitstuk': KeuzelijstWaarde(invulwaarde='aansluitstuk',
                                         label='aansluitstuk',
                                         definitie='aansluitstuk',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulpstukType/aansluitstuk'),
        'bochtstuk': KeuzelijstWaarde(invulwaarde='bochtstuk',
                                      label='bochtstuk',
                                      definitie='bochtstuk',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulpstukType/bochtstuk')
    }

