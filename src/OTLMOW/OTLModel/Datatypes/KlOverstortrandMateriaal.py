# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOverstortrandMateriaal(KeuzelijstField):
    """De materialen van de overstortrand."""
    naam = 'KlOverstortrandMateriaal'
    label = 'Overstortrand materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOverstortrandMateriaal'
    definition = 'De materialen van de overstortrand.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOverstortrandMateriaal'
    options = {
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='hout',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Een overstortrand uit hout.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverstortrandMateriaal/hout'),
        'inox': KeuzelijstWaarde(invulwaarde='inox',
                                 label='inox',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Een overstortrand uit inox.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverstortrandMateriaal/inox'),
        'metselwerk': KeuzelijstWaarde(invulwaarde='metselwerk',
                                       label='metselwerk',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Een overstortrand uit metselwerk.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverstortrandMateriaal/metselwerk')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlOverstortrandMateriaal.get_dummy_data()

