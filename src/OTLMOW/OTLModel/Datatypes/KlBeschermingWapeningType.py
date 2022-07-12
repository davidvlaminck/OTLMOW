# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeschermingWapeningType(KeuzelijstField):
    """De mogelijke wapeningen gebruikt bij de oa. fundering (wapeningsnet,geotextiel,geogrids)."""
    naam = 'KlBeschermingWapeningType'
    label = 'Bescherming wapening type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBeschermingWapeningType'
    definition = 'De mogelijke wapeningen gebruikt bij de oa. fundering (wapeningsnet,geotextiel,geogrids).'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeschermingWapeningType'
    options = {
        'gelast-geplastificeerd-gaas': KeuzelijstWaarde(invulwaarde='gelast-geplastificeerd-gaas',
                                                        label='gelast geplastificeerd gaas',
                                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                        definitie='gelast geplastificeerd gaas',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermingWapeningType/gelast-geplastificeerd-gaas'),
        'geogrids': KeuzelijstWaarde(invulwaarde='geogrids',
                                     label='geogrids',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Een roosterweefsel dat als een soort funderingsrooster wordt toegepast',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermingWapeningType/geogrids'),
        'honinggraatstructuur': KeuzelijstWaarde(invulwaarde='honinggraatstructuur',
                                                 label='honinggraatstructuur',
                                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                 definitie='Een wapening_bescherming met honinggraatstructuur.',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermingWapeningType/honinggraatstructuur'),
        'wapeningsnet': KeuzelijstWaarde(invulwaarde='wapeningsnet',
                                         label='wapeningsnet',
                                         status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie='Keuzelijst voor de wapening gebruikt bij de fundering (wapeningsnet,geotextiel,geogrids)',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermingWapeningType/wapeningsnet')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBeschermingWapeningType.get_dummy_data()

