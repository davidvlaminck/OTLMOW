# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlServicePrioriteit(KeuzelijstField):
    """Het prioriteitsniveau dat aangeeft hoe dringend iets moet onderhouden/gerepareerd worden"""
    naam = 'KlServicePrioriteit'
    label = 'Serviceprioriteit'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlServicePrioriteit'
    definition = 'Het prioriteitsniveau dat aangeeft hoe dringend iets moet onderhouden/gerepareerd worden'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlServicePrioriteit'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

