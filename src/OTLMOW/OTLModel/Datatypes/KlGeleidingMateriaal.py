# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGeleidingMateriaal(KeuzelijstField):
    """Materialen voor de geleidingwand om kleinere wilde dieren te geleiden."""
    naam = 'KlGeleidingMateriaal'
    label = 'Geleiding materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGeleidingMateriaal'
    definition = 'Materialen voor de geleidingwand om kleinere wilde dieren te geleiden.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGeleidingMateriaal'
    options = {
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  definitie='Geleiding bestaande uit een betonnen wand.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeleidingMateriaal/beton'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='kunststof',
                                      definitie='Geleiding bestaande uit een kunststoffen wand.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeleidingMateriaal/kunststof'),
        'metaal': KeuzelijstWaarde(invulwaarde='metaal',
                                   label='metaal',
                                   definitie='Geleiding bestaande uit een metalen wand.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeleidingMateriaal/metaal')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlGeleidingMateriaal.get_dummy_data()

