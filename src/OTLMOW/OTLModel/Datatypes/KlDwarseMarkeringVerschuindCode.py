# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDwarseMarkeringVerschuindCode(KeuzelijstField):
    """Codes van de schuine dwarse markering."""
    naam = 'KlDwarseMarkeringVerschuindCode'
    label = 'Dwarse markering code verschuind'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDwarseMarkeringVerschuindCode'
    definition = 'Codes van de schuine dwarse markering.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDwarseMarkeringVerschuindCode'
    options = {
        'FOP-sch': KeuzelijstWaarde(invulwaarde='FOP-sch',
                                    label='FOP-sch',
                                    definitie='Fietsoversteekplaats met blokken schuin',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringVerschuindCode/FOP-sch')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlDwarseMarkeringVerschuindCode.get_dummy_data()

