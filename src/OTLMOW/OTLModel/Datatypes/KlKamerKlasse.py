# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKamerKlasse(KeuzelijstField):
    """De stabiliteitsklasse van de kamer."""
    naam = 'KlKamerKlasse'
    label = 'Kamer klasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKamerKlasse'
    definition = 'De stabiliteitsklasse van de kamer.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKamerKlasse'
    options = {
        'klasse-1': KeuzelijstWaarde(invulwaarde='klasse-1',
                                     label='klasse 1',
                                     definitie='klasse 1',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKamerKlasse/klasse-1'),
        'klasse-2': KeuzelijstWaarde(invulwaarde='klasse-2',
                                     label='klasse 2',
                                     definitie='klasse 2',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKamerKlasse/klasse-2')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlKamerKlasse.get_dummy_data()

