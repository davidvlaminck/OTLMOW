# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEnergiemeterDNBUurtarief(KeuzelijstField):
    """Type uurtarief vb enkelvoudig, dubbelvoudig,..."""
    naam = 'KlEnergiemeterDNBUurtarief'
    label = 'Energiemeter DNB uurtarief'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEnergiemeterDNBUurtarief'
    definition = 'Type uurtarief vb enkelvoudig, dubbelvoudig,...'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEnergiemeterDNBUurtarief'
    options = {
        'dubbelvoudig': KeuzelijstWaarde(invulwaarde='dubbelvoudig',
                                         label='dubbelvoudig',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEnergiemeterDNBUurtarief/dubbelvoudig'),
        'dubbelvoudig-maar-enkelvoudig-gebruikt': KeuzelijstWaarde(invulwaarde='dubbelvoudig-maar-enkelvoudig-gebruikt',
                                                                   label='dubbelvoudig maar enkelvoudig gebruikt',
                                                                   status='ingebruik',
                                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEnergiemeterDNBUurtarief/dubbelvoudig-maar-enkelvoudig-gebruikt'),
        'enkelvoudig': KeuzelijstWaarde(invulwaarde='enkelvoudig',
                                        label='enkelvoudig',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEnergiemeterDNBUurtarief/enkelvoudig')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

