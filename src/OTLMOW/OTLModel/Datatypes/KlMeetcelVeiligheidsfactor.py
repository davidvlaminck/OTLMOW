# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMeetcelVeiligheidsfactor(KeuzelijstField):
    """Verhouding tussen de toegekende primaire limietstroom van de meetcel en de toegekende primaire stroom."""
    naam = 'KlMeetcelVeiligheidsfactor'
    label = 'Meetcel veiligheidsfactor'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMeetcelVeiligheidsfactor'
    definition = 'Verhouding tussen de toegekende primaire limietstroom van de meetcel en de toegekende primaire stroom.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMeetcelVeiligheidsfactor'
    options = {
        'fS-5': KeuzelijstWaarde(invulwaarde='fS-5',
                                 label='fS 5',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeetcelVeiligheidsfactor/fS-5')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlMeetcelVeiligheidsfactor.get_dummy_data()

