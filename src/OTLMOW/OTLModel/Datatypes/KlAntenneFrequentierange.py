# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAntenneFrequentierange(KeuzelijstField):
    """Keuzelijst met frequentiebanden aan waarbinnen een antenne gebruikt kan worden."""
    naam = 'KlAntenneFrequentierange'
    label = 'Antenne frequentierange'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAntenneFrequentierange'
    definition = 'Keuzelijst met frequentiebanden aan waarbinnen een antenne gebruikt kan worden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAntenneFrequentierange'
    options = {
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlAntenneFrequentierange.get_dummy_data()

