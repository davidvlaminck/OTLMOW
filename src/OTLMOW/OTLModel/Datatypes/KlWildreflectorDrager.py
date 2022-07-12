# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWildreflectorDrager(KeuzelijstField):
    """Mogelijke dragers van een wildreflector."""
    naam = 'KlWildreflectorDrager'
    label = 'Wildreflector drager'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWildreflectorDrager'
    definition = 'Mogelijke dragers van een wildreflector.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWildreflectorDrager'
    options = {
        'houten-paal': KeuzelijstWaarde(invulwaarde='houten-paal',
                                        label='houten paal',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='houten paal als drager.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWildreflectorDrager/houten-paal'),
        'metalen-paal': KeuzelijstWaarde(invulwaarde='metalen-paal',
                                         label='metalen paal',
                                         status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie='metalen paal als drager.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWildreflectorDrager/metalen-paal')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlWildreflectorDrager.get_dummy_data()

