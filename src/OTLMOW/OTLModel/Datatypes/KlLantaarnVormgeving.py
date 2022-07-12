# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLantaarnVormgeving(KeuzelijstField):
    """Keuzelijst met verschillende types vormgeving voor een seinlantaarn."""
    naam = 'KlLantaarnVormgeving'
    label = 'Lantaarn vormgeving'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlLantaarnVormgeving'
    definition = 'Keuzelijst met verschillende types vormgeving voor een seinlantaarn.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLantaarnVormgeving'
    options = {
        'bijzondere-esthetische-vormgeving': KeuzelijstWaarde(invulwaarde='bijzondere-esthetische-vormgeving',
                                                              label='bijzondere esthetische vormgeving',
                                                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLantaarnVormgeving/bijzondere-esthetische-vormgeving'),
        'standaard-vormgeving': KeuzelijstWaarde(invulwaarde='standaard-vormgeving',
                                                 label='standaard vormgeving',
                                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLantaarnVormgeving/standaard-vormgeving')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlLantaarnVormgeving.get_dummy_data()

