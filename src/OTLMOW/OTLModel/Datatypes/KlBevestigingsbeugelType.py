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
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBevestigingsbeugelType'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

