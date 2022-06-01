# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSeinlantaarnDiameter(KeuzelijstField):
    """Keuzelijst met de verschillende voorkomende diameter-waarden voor Seinlantaarn."""
    naam = 'KlSeinlantaarnDiameter'
    label = 'Seinlantaarn diameter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlSeinlantaarnDiameter'
    definition = 'Keuzelijst met de verschillende voorkomende diameter-waarden voor Seinlantaarn.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSeinlantaarnDiameter'
    options = {
        '100': KeuzelijstWaarde(invulwaarde='100',
                                label='100',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinlantaarnDiameter/100'),
        '200': KeuzelijstWaarde(invulwaarde='200',
                                label='200',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinlantaarnDiameter/200'),
        '300': KeuzelijstWaarde(invulwaarde='300',
                                label='300',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinlantaarnDiameter/300')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlSeinlantaarnDiameter.get_dummy_data()

