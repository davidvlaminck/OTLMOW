# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFolieType(KeuzelijstField):
    """Types van folie."""
    naam = 'KlFolieType'
    label = 'Folie type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFolieType'
    definition = 'Types van folie.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFolieType'
    options = {
        'folietype-1': KeuzelijstWaarde(invulwaarde='folietype-1',
                                        label='folietype 1',
                                        definitie='folietype 1',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFolieType/folietype-1'),
        'folietype-2': KeuzelijstWaarde(invulwaarde='folietype-2',
                                        label='folietype 2',
                                        definitie='folietype 2',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFolieType/folietype-2'),
        'folietype-3a': KeuzelijstWaarde(invulwaarde='folietype-3a',
                                         label='folietype 3a',
                                         definitie='folietype 3a',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFolieType/folietype-3a'),
        'folietype-3a-en-3b': KeuzelijstWaarde(invulwaarde='folietype-3a-en-3b',
                                               label='folietype 3a en 3b',
                                               definitie='folietype 3a en 3b',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFolieType/folietype-3a-en-3b'),
        'folietype-3b': KeuzelijstWaarde(invulwaarde='folietype-3b',
                                         label='folietype 3b',
                                         definitie='folietype 3b',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFolieType/folietype-3b')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlFolieType.get_dummy_data()

