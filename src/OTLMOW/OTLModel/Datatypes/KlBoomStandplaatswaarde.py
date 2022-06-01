# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomStandplaatswaarde(KeuzelijstField):
    """De verschillende opties van de standplaatswaarde voor een boom."""
    naam = 'KlBoomStandplaatswaarde'
    label = 'Boom standplaatswaarde'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomStandplaatswaarde'
    definition = 'De verschillende opties van de standplaatswaarde voor een boom.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomStandplaatswaarde'
    options = {
        '0.6': KeuzelijstWaarde(invulwaarde='0.6',
                                label='0.6',
                                definitie='Landelijk gebied',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomStandplaatswaarde/0.6'),
        '0.7': KeuzelijstWaarde(invulwaarde='0.7',
                                label='0.7',
                                definitie='Overgangszone: bebouwde kom - landelijk gebied',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomStandplaatswaarde/0.7'),
        '0.8': KeuzelijstWaarde(invulwaarde='0.8',
                                label='0.8',
                                definitie='Open en halfopen bebouwing',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomStandplaatswaarde/0.8'),
        '0.9': KeuzelijstWaarde(invulwaarde='0.9',
                                label='0.9',
                                definitie='Gesloten bebouwing',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomStandplaatswaarde/0.9'),
        '1.0': KeuzelijstWaarde(invulwaarde='1.0',
                                label='1.0',
                                definitie='Sterk verstedelijkte stads- of dorpskern',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomStandplaatswaarde/1.0')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBoomStandplaatswaarde.get_dummy_data()

