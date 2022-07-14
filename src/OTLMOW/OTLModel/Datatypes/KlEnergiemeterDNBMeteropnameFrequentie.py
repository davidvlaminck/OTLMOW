# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEnergiemeterDNBMeteropnameFrequentie(KeuzelijstField):
    """Frequentie waarmee de meterstand opgenomen wordt door de netbeheerder."""
    naam = 'KlEnergiemeterDNBMeteropnameFrequentie'
    label = 'Energiemeter DNB meteropname frequentie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEnergiemeterDNBMeteropnameFrequentie'
    definition = 'Frequentie waarmee de meterstand opgenomen wordt door de netbeheerder.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEnergiemeterDNBMeteropnameFrequentie'
    options = {
        'AMR': KeuzelijstWaarde(invulwaarde='AMR',
                                label='AMR',
                                status='ingebruik',
                                definitie='automatische meter reading',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEnergiemeterDNBMeteropnameFrequentie/AMR'),
        'MMR': KeuzelijstWaarde(invulwaarde='MMR',
                                label='MMR',
                                status='ingebruik',
                                definitie='manuele meter opname',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEnergiemeterDNBMeteropnameFrequentie/MMR'),
        'YMR': KeuzelijstWaarde(invulwaarde='YMR',
                                label='YMR',
                                status='ingebruik',
                                definitie='jaarlijkse meter opname',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEnergiemeterDNBMeteropnameFrequentie/YMR')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

