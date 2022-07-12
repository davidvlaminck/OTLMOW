# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMozaiekkeiFormaat(KeuzelijstField):
    """Formaten van de mozaïekkei."""
    naam = 'KlMozaiekkeiFormaat'
    label = 'Mozaiekkei formaat'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMozaiekkeiFormaat'
    definition = 'Formaten van de mozaïekkei.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMozaiekkeiFormaat'
    options = {
        'bestratingen-van-mozaïekkeien-van-het-1ste-formaat': KeuzelijstWaarde(invulwaarde='bestratingen-van-mozaïekkeien-van-het-1ste-formaat',
                                                                               label='bestratingen van mozaïekkeien van het 1ste formaat',
                                                                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                               definitie='Bestratingen van mozaïekkeien van het 1ste formaat',
                                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMozaiekkeiFormaat/bestratingen-van-mozaïekkeien-van-het-1ste-formaat'),
        'bestratingen-van-mozaïekkeien-van-het-2de-formaat': KeuzelijstWaarde(invulwaarde='bestratingen-van-mozaïekkeien-van-het-2de-formaat',
                                                                              label='bestratingen van mozaïekkeien van het 2de formaat',
                                                                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                              definitie='Bestratingen van mozaïekkeien van het 2de formaat',
                                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMozaiekkeiFormaat/bestratingen-van-mozaïekkeien-van-het-2de-formaat'),
        'bestratingen-van-mozaïekkeien-van-het-3de-formaat': KeuzelijstWaarde(invulwaarde='bestratingen-van-mozaïekkeien-van-het-3de-formaat',
                                                                              label='bestratingen van mozaïekkeien van het 3de formaat',
                                                                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                              definitie='Bestratingen van mozaïekkeien van het 3de formaat',
                                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMozaiekkeiFormaat/bestratingen-van-mozaïekkeien-van-het-3de-formaat'),
        'bestratingen-van-mozaïekkeien-van-het-4de-formaat': KeuzelijstWaarde(invulwaarde='bestratingen-van-mozaïekkeien-van-het-4de-formaat',
                                                                              label='bestratingen van mozaïekkeien van het 4de formaat',
                                                                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                              definitie='Bestratingen van mozaïekkeien van het 4de formaat',
                                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMozaiekkeiFormaat/bestratingen-van-mozaïekkeien-van-het-4de-formaat'),
        'bestratingen-van-mozaïekkeien-van-het-5de-formaat': KeuzelijstWaarde(invulwaarde='bestratingen-van-mozaïekkeien-van-het-5de-formaat',
                                                                              label='bestratingen van mozaïekkeien van het 5de formaat',
                                                                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                              definitie='Bestratingen van mozaïekkeien van het 5de formaat',
                                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMozaiekkeiFormaat/bestratingen-van-mozaïekkeien-van-het-5de-formaat')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlMozaiekkeiFormaat.get_dummy_data()

