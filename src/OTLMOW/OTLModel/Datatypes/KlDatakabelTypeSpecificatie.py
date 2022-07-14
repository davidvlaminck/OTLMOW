# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDatakabelTypeSpecificatie(KeuzelijstField):
    """Een verdere specificatie van het type van de datakabel volgens een vaste lijst om bv. de brandklasse mee te geven."""
    naam = 'KlDatakabelTypeSpecificatie'
    label = 'Datakabel type specificatie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDatakabelTypeSpecificatie'
    definition = 'Een verdere specificatie van het type van de datakabel volgens een vaste lijst om bv. de brandklasse mee te geven.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDatakabelTypeSpecificatie'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

