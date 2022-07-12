# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVormSchermelement(KeuzelijstField):
    """Deze keuzelijst geeft aan of het schermelement recht of gebogen is."""
    naam = 'KlVormSchermelement'
    label = 'Vorm schermelement'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVormSchermelement'
    definition = 'Deze keuzelijst geeft aan of het schermelement recht of gebogen is.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVormSchermelement'
    options = {
        'gebogen': KeuzelijstWaarde(invulwaarde='gebogen',
                                    label='gebogen',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='gebogen',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormSchermelement/gebogen'),
        'recht': KeuzelijstWaarde(invulwaarde='recht',
                                  label='recht',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='recht',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormSchermelement/recht')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlVormSchermelement.get_dummy_data()

