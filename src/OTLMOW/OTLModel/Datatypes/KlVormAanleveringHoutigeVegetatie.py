# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVormAanleveringHoutigeVegetatie(KeuzelijstField):
    """De wijze waarop het plantgoed wordt aangeleverd."""
    naam = 'KlVormAanleveringHoutigeVegetatie'
    label = 'Vorm aanlevering houtige vegetatie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVormAanleveringHoutigeVegetatie'
    definition = 'De wijze waarop het plantgoed wordt aangeleverd.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVormAanleveringHoutigeVegetatie'
    options = {
        'bomen': KeuzelijstWaarde(invulwaarde='bomen',
                                  label='bomen',
                                  status='ingebruik',
                                  definitie='Aanlevering van houtige vegetatie in de vorm van bomen.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormAanleveringHoutigeVegetatie/bomen'),
        'bosgoed': KeuzelijstWaarde(invulwaarde='bosgoed',
                                    label='bosgoed',
                                    status='ingebruik',
                                    definitie='Aanlevering van houtige vegetatie in de vorm van bosgoed.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormAanleveringHoutigeVegetatie/bosgoed'),
        'meerstammige-bomen': KeuzelijstWaarde(invulwaarde='meerstammige-bomen',
                                               label='meerstammige bomen',
                                               status='ingebruik',
                                               definitie='Aanlevering van houtige vegetatie in de vorm van meerstammige bomen.',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormAanleveringHoutigeVegetatie/meerstammige-bomen'),
        'poten': KeuzelijstWaarde(invulwaarde='poten',
                                  label='poten',
                                  status='ingebruik',
                                  definitie='Aanlevering van houtige vegetatie in de vorm van poten.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormAanleveringHoutigeVegetatie/poten'),
        'veer': KeuzelijstWaarde(invulwaarde='veer',
                                 label='veer',
                                 status='ingebruik',
                                 definitie='Aanlevering van houtige vegetatie in de vorm van veer.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormAanleveringHoutigeVegetatie/veer')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlVormAanleveringHoutigeVegetatie.get_dummy_data()

