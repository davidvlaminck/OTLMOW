# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgSnelheidsregime(KeuzelijstField):
    """De snelheidsregimes met variabele mogelijkeid."""
    naam = 'KlAlgSnelheidsregime'
    label = 'Snelheidsregime'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAlgSnelheidsregime'
    definition = 'De snelheidsregimes met variabele mogelijkeid.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgSnelheidsregime'
    options = {
        '120': KeuzelijstWaarde(invulwaarde='120',
                                label='120',
                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='120 km/h.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/120'),
        '30': KeuzelijstWaarde(invulwaarde='30',
                               label='30',
                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='30 km/h.',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/30'),
        '50': KeuzelijstWaarde(invulwaarde='50',
                               label='50',
                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='50 km/h.',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/50'),
        '60': KeuzelijstWaarde(invulwaarde='60',
                               label='60',
                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='60 km/h.',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/60'),
        '70': KeuzelijstWaarde(invulwaarde='70',
                               label='70',
                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='70 km/h.',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/70'),
        '80': KeuzelijstWaarde(invulwaarde='80',
                               label='80',
                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='80 km/h.',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/80'),
        '90': KeuzelijstWaarde(invulwaarde='90',
                               label='90',
                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='90 km/h.',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/90'),
        'variabel': KeuzelijstWaarde(invulwaarde='variabel',
                                     label='variabel',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Variabele ingave.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/variabel')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlAlgSnelheidsregime.get_dummy_data()

