# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDwarseMarkeringVerschuindSoort(KeuzelijstField):
    """Soorten van de schuine dwarse markering."""
    naam = 'KlDwarseMarkeringVerschuindSoort'
    label = 'Dwarse markering soort verschuind'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDwarseMarkeringVerschuindSoort'
    definition = 'Soorten van de schuine dwarse markering.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDwarseMarkeringVerschuindSoort'
    options = {
        'fietsoversteekplaats-met-blokken-(FOP)-schuin': KeuzelijstWaarde(invulwaarde='fietsoversteekplaats-met-blokken-(FOP)-schuin',
                                                                          label='fietsoversteekplaats met blokken (FOP) schuin',
                                                                          definitie='Een oversteekplaats voor fietsers gemarkeerd door witte parallellogrammen.',
                                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringVerschuindSoort/fietsoversteekplaats-met-blokken-(FOP)-schuin')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlDwarseMarkeringVerschuindSoort.get_dummy_data()

