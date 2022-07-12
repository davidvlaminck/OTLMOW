# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAntiparkeerpaalMateriaal(KeuzelijstField):
    """Bepaling van het vervaardigingsmateriaal van de antiparkeerpaal."""
    naam = 'KlAntiparkeerpaalMateriaal'
    label = 'Antiparkeerpaal materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAntiparkeerpaalMateriaal'
    definition = 'Bepaling van het vervaardigingsmateriaal van de antiparkeerpaal.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAntiparkeerpaalMateriaal'
    options = {
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='hout',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Keuze hout voor het antiparkeerpaal materiaal.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAntiparkeerpaalMateriaal/hout'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='kunststof',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Keuze kunststof voor het antiparkeerpaal materiaal.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAntiparkeerpaalMateriaal/kunststof'),
        'metaal': KeuzelijstWaarde(invulwaarde='metaal',
                                   label='metaal',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Keuze metaal voor het antiparkeerpaal materiaal.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAntiparkeerpaalMateriaal/metaal')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlAntiparkeerpaalMateriaal.get_dummy_data()

