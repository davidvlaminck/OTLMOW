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
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDraagconstructieDwarsdoorsnede'
    options = {
        'octagonaal': KeuzelijstWaarde(invulwaarde='octagonaal',
                                       label='octagonaal',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagconstructieDwarsdoorsnede/octagonaal'),
        'rond': KeuzelijstWaarde(invulwaarde='rond',
                                 label='rond',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagconstructieDwarsdoorsnede/rond'),
        'vierkant': KeuzelijstWaarde(invulwaarde='vierkant',
                                     label='vierkant',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagconstructieDwarsdoorsnede/vierkant')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

