# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVriLusFunctie(KeuzelijstField):
    """Keuzelijst met verschillende types detectielussen naar functie."""
    naam = 'KlVriLusFunctie'
    label = 'VRI-lus functie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVriLusFunctie'
    definition = 'Keuzelijst met verschillende types detectielussen naar functie.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVriLusFunctie'
    options = {
        'KAR-inmeldlus': KeuzelijstWaarde(invulwaarde='KAR-inmeldlus',
                                          label='KAR inmeldlus',
                                          status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/KAR-inmeldlus'),
        'KAR-uitmeldlus': KeuzelijstWaarde(invulwaarde='KAR-uitmeldlus',
                                           label='KAR uitmeldlus',
                                           status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/KAR-uitmeldlus'),
        'afstandslus': KeuzelijstWaarde(invulwaarde='afstandslus',
                                        label='afstandslus',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/afstandslus'),
        'filelus': KeuzelijstWaarde(invulwaarde='filelus',
                                    label='filelus',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/filelus'),
        'hiaatlus': KeuzelijstWaarde(invulwaarde='hiaatlus',
                                     label='hiaatlus',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/hiaatlus'),
        'stopstreeplus': KeuzelijstWaarde(invulwaarde='stopstreeplus',
                                          label='stopstreeplus',
                                          status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/stopstreeplus')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlVriLusFunctie.get_dummy_data()

