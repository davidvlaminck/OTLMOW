# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHulpstukType(KeuzelijstField):
    """Het type van het hulpstuk."""
    naam = 'KlHulpstukType'
    label = 'Hulpstuk type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHulpstukType'
    definition = 'Het type van het hulpstuk.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHulpstukType'
    options = {
        'T-stuk': KeuzelijstWaarde(invulwaarde='T-stuk',
                                   label='T-stuk',
                                   status='ingebruik',
                                   definitie='T-stuk',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulpstukType/T-stuk'),
        'Y-stuk': KeuzelijstWaarde(invulwaarde='Y-stuk',
                                   label='Y-stuk',
                                   status='ingebruik',
                                   definitie='Y-stuk',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulpstukType/Y-stuk'),
        'aansluitstuk': KeuzelijstWaarde(invulwaarde='aansluitstuk',
                                         label='aansluitstuk',
                                         status='ingebruik',
                                         definitie='aansluitstuk',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulpstukType/aansluitstuk'),
        'bochtstuk': KeuzelijstWaarde(invulwaarde='bochtstuk',
                                      label='bochtstuk',
                                      status='ingebruik',
                                      definitie='bochtstuk',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulpstukType/bochtstuk')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

