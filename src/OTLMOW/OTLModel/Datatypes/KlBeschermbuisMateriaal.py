# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeschermbuisMateriaal(KeuzelijstField):
    """Keuzelijst voor het bepalen van het materiaal van de beschermbuis."""
    naam = 'KlBeschermbuisMateriaal'
    label = 'Beschermbuis materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBeschermbuisMateriaal'
    definition = 'Keuzelijst voor het bepalen van het materiaal van de beschermbuis.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeschermbuisMateriaal'
    options = {
        'hdpe': KeuzelijstWaarde(invulwaarde='hdpe',
                                 label='HDPE',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisMateriaal/hdpe'),
        'hdpe-pn10': KeuzelijstWaarde(invulwaarde='hdpe-pn10',
                                      label='HDPE PN10',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisMateriaal/hdpe-pn10'),
        'pvc': KeuzelijstWaarde(invulwaarde='pvc',
                                label='PVC',
                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisMateriaal/pvc'),
        'rvs': KeuzelijstWaarde(invulwaarde='rvs',
                                label='RVS',
                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisMateriaal/rvs')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBeschermbuisMateriaal.get_dummy_data()

