# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSeinbrugType(KeuzelijstField):
    """Types van seinbrug."""
    naam = 'KlSeinbrugType'
    label = 'Seinbrug type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSeinbrugType'
    definition = 'Types van seinbrug.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSeinbrugType'
    options = {
        'enkeleLigger': KeuzelijstWaarde(invulwaarde='enkeleLigger',
                                         label='enkeleLigger',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinbrugType/enkeleLigger'),
        'koker': KeuzelijstWaarde(invulwaarde='koker',
                                  label='koker',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinbrugType/koker'),
        'nietDoorlopendeBuis': KeuzelijstWaarde(invulwaarde='nietDoorlopendeBuis',
                                                label='nietDoorlopendeBuis',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinbrugType/nietDoorlopendeBuis'),
        'vakwerk': KeuzelijstWaarde(invulwaarde='vakwerk',
                                    label='vakwerk',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinbrugType/vakwerk')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlSeinbrugType.get_dummy_data()

