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
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeschermbuisMateriaal'
    options = {
        'hdpe': KeuzelijstWaarde(invulwaarde='hdpe',
                                 label='HDPE',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisMateriaal/hdpe'),
        'hdpe-pn10': KeuzelijstWaarde(invulwaarde='hdpe-pn10',
                                      label='HDPE PN10',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisMateriaal/hdpe-pn10'),
        'pvc': KeuzelijstWaarde(invulwaarde='pvc',
                                label='PVC',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisMateriaal/pvc'),
        'rvs': KeuzelijstWaarde(invulwaarde='rvs',
                                label='RVS',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisMateriaal/rvs')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

