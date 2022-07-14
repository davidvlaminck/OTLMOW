# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHSBeveiligingscelSchakelmateriaalType(KeuzelijstField):
    """Type van schakelmateriaal."""
    naam = 'KlHSBeveiligingscelSchakelmateriaalType'
    label = 'HS-beveiligingscel schakelmateriaal type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHSBeveiligingscelSchakelmateriaalType'
    definition = 'Type van schakelmateriaal.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHSBeveiligingscelSchakelmateriaalType'
    options = {
        'RMU-2KT': KeuzelijstWaarde(invulwaarde='RMU-2KT',
                                    label='RMU 2KT',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelSchakelmateriaalType/RMU-2KT'),
        'RMU-3KT': KeuzelijstWaarde(invulwaarde='RMU-3KT',
                                    label='RMU 3KT',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelSchakelmateriaalType/RMU-3KT'),
        'metaalomsloten-celstruktuur': KeuzelijstWaarde(invulwaarde='metaalomsloten-celstruktuur',
                                                        label='metaalomsloten celstruktuur',
                                                        status='ingebruik',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelSchakelmateriaalType/metaalomsloten-celstruktuur'),
        'metal-clad-schakelvelden': KeuzelijstWaarde(invulwaarde='metal-clad-schakelvelden',
                                                     label='metal-clad schakelvelden',
                                                     status='ingebruik',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelSchakelmateriaalType/metal-clad-schakelvelden'),
        'modulaire-schakelvelden': KeuzelijstWaarde(invulwaarde='modulaire-schakelvelden',
                                                    label='modulaire schakelvelden',
                                                    status='ingebruik',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelSchakelmateriaalType/modulaire-schakelvelden'),
        'open-celstruktuur': KeuzelijstWaarde(invulwaarde='open-celstruktuur',
                                              label='open celstruktuur',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelSchakelmateriaalType/open-celstruktuur')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

