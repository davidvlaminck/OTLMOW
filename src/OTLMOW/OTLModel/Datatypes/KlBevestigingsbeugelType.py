# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBevestigingsbeugelType(KeuzelijstField):
    """Types van bevestigingsbeugel."""
    naam = 'KlBevestigingsbeugelType'
    label = 'Bevestigingsbeugel type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBevestigingsbeugelType'
    definition = 'Types van bevestigingsbeugel.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBevestigingsbeugelType'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBevestigingsbeugelType.get_dummy_data()

