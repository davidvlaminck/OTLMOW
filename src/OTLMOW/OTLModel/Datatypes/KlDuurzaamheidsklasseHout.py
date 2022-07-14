# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDuurzaamheidsklasseHout(KeuzelijstField):
    """De resistentie van het kernhout tegen ongunstige omstandigheden."""
    naam = 'KlDuurzaamheidsklasseHout'
    label = 'Duurzaamheidsklasse van hout'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlDuurzaamheidsklasseHout'
    definition = 'De resistentie van het kernhout tegen ongunstige omstandigheden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDuurzaamheidsklasseHout'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

