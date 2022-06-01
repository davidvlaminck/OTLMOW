# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDraagconstructieDwarsdoorsnede(KeuzelijstField):
    """Lijst van mogelijke vormen van dwarsdoorsnedes van een draagconstructie."""
    naam = 'KlDraagconstructieDwarsdoorsnede'
    label = 'Draagconstructie dwarsdoorsnede'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDraagconstructieDwarsdoorsnede'
    definition = 'Lijst van mogelijke vormen van dwarsdoorsnedes van een draagconstructie.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDraagconstructieDwarsdoorsnede'
    options = {
        'octagonaal': KeuzelijstWaarde(invulwaarde='octagonaal',
                                       label='octagonaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagconstructieDwarsdoorsnede/octagonaal'),
        'rond': KeuzelijstWaarde(invulwaarde='rond',
                                 label='rond',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagconstructieDwarsdoorsnede/rond'),
        'vierkant': KeuzelijstWaarde(invulwaarde='vierkant',
                                     label='vierkant',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagconstructieDwarsdoorsnede/vierkant')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlDraagconstructieDwarsdoorsnede.get_dummy_data()

