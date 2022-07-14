# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSterkteklasseHout(KeuzelijstField):
    """De klasse die de maximale belasting van het hout aangeeft. Gebruik letter C voor naaldhout en D voor loofhout, gevolgd door een getal dat betrekking heeft op de karakteristieke buigspanning."""
    naam = 'KlSterkteklasseHout'
    label = 'Sterkteklasse van hout'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlSterkteklasseHout'
    definition = 'De klasse die de maximale belasting van het hout aangeeft. Gebruik letter C voor naaldhout en D voor loofhout, gevolgd door een getal dat betrekking heeft op de karakteristieke buigspanning.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSterkteklasseHout'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

