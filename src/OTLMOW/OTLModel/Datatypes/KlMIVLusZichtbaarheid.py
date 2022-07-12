# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMIVLusZichtbaarheid(KeuzelijstField):
    """Is de lus zichtbaar in het wegdek of bedenkt door een toplaag."""
    naam = 'KlMIVLusZichtbaarheid'
    label = 'MIV-lus zichtbaarheid'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMIVLusZichtbaarheid'
    definition = 'Is de lus zichtbaar in het wegdek of bedenkt door een toplaag.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMIVLusZichtbaarheid'
    options = {
        'onderlaag': KeuzelijstWaarde(invulwaarde='onderlaag',
                                      label='onderlaag',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVLusZichtbaarheid/onderlaag'),
        'toplaag': KeuzelijstWaarde(invulwaarde='toplaag',
                                    label='toplaag',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVLusZichtbaarheid/toplaag')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlMIVLusZichtbaarheid.get_dummy_data()

