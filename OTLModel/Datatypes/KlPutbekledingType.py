# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPutbekledingType(KeuzelijstField):
    """Types van putbekleding."""
    naam = 'KlPutbekledingType'
    label = 'Putbekleding type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPutbekledingType'
    definition = 'Types van putbekleding.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPutbekledingType'
    options = {
        'solventvrije-kunsthars': KeuzelijstWaarde(invulwaarde='solventvrije-kunsthars',
                                                   label='solventvrije kunsthars',
                                                   definitie='solventvrije kunsthars',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutbekledingType/solventvrije-kunsthars'),
        'solventvrije-vezelversterkte-epoxyhars': KeuzelijstWaarde(invulwaarde='solventvrije-vezelversterkte-epoxyhars',
                                                                   label='solventvrije vezelversterkte epoxyhars',
                                                                   definitie='solventvrije vezelversterkte epoxyhars',
                                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutbekledingType/solventvrije-vezelversterkte-epoxyhars')
    }

