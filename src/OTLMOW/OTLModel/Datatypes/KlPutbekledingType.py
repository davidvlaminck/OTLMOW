# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPutbekledingType(KeuzelijstField):
    """Types van putbekleding."""
    naam = 'KlPutbekledingType'
    label = 'Putbekleding type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPutbekledingType'
    definition = 'Types van putbekleding.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPutbekledingType'
    options = {
        'solventvrije-kunsthars': KeuzelijstWaarde(invulwaarde='solventvrije-kunsthars',
                                                   label='solventvrije kunsthars',
                                                   status='ingebruik',
                                                   definitie='solventvrije kunsthars',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutbekledingType/solventvrije-kunsthars'),
        'solventvrije-vezelversterkte-epoxyhars': KeuzelijstWaarde(invulwaarde='solventvrije-vezelversterkte-epoxyhars',
                                                                   label='solventvrije vezelversterkte epoxyhars',
                                                                   status='ingebruik',
                                                                   definitie='solventvrije vezelversterkte epoxyhars',
                                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutbekledingType/solventvrije-vezelversterkte-epoxyhars')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

