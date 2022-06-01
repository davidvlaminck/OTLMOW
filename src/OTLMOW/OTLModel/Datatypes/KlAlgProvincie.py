# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgProvincie(KeuzelijstField):
    """Lijst van provincies in Vlaanderen."""
    naam = 'KlAlgProvincie'
    label = 'Provincie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgProvincie'
    definition = 'Lijst van provincies in Vlaanderen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgProvincie'
    options = {
        'antwerpen': KeuzelijstWaarde(invulwaarde='antwerpen',
                                      label='antwerpen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgProvincie/antwerpen'),
        'limburg': KeuzelijstWaarde(invulwaarde='limburg',
                                    label='limburg',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgProvincie/limburg'),
        'oost-Vlaanderen': KeuzelijstWaarde(invulwaarde='oost-Vlaanderen',
                                            label='oost-Vlaanderen',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgProvincie/oost-Vlaanderen'),
        'vlaams-Brabant': KeuzelijstWaarde(invulwaarde='vlaams-Brabant',
                                           label='vlaams-Brabant',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgProvincie/vlaams-Brabant'),
        'west-Vlaanderen': KeuzelijstWaarde(invulwaarde='west-Vlaanderen',
                                            label='west-Vlaanderen',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgProvincie/west-Vlaanderen')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlAIMToestand.get_dummy_data()

