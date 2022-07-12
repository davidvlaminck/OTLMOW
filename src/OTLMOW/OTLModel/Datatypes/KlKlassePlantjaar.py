# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKlassePlantjaar(KeuzelijstField):
    """Het geschatte tijdsinterval waarin de boom is aangeplant."""
    naam = 'KlKlassePlantjaar'
    label = 'Klasse plantjaar'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKlassePlantjaar'
    definition = 'Het geschatte tijdsinterval waarin de boom is aangeplant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKlassePlantjaar'
    options = {
        '1880-1900': KeuzelijstWaarde(invulwaarde='1880-1900',
                                      label='1880-1900',
                                      status='ingebruik',
                                      definitie='De boom is aangeplant tussen 1880 en 1900.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKlassePlantjaar/1880-1900'),
        '1900-1920': KeuzelijstWaarde(invulwaarde='1900-1920',
                                      label='1900-1920',
                                      status='ingebruik',
                                      definitie='De boom is aangeplant tussen 1900 en 1920.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKlassePlantjaar/1900-1920'),
        '1920-1940': KeuzelijstWaarde(invulwaarde='1920-1940',
                                      label='1920-1940',
                                      status='ingebruik',
                                      definitie='De boom is aangeplant tussen 1920 en 1940.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKlassePlantjaar/1920-1940'),
        '1940-1960': KeuzelijstWaarde(invulwaarde='1940-1960',
                                      label='1940-1960',
                                      status='ingebruik',
                                      definitie='De boom is aangeplant tussen 1940 en 1960.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKlassePlantjaar/1940-1960'),
        '1960-1980': KeuzelijstWaarde(invulwaarde='1960-1980',
                                      label='1960-1980',
                                      status='ingebruik',
                                      definitie='De boom is aangeplant tussen 1960 en 1980.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKlassePlantjaar/1960-1980'),
        '1980-2000': KeuzelijstWaarde(invulwaarde='1980-2000',
                                      label='1980-2000',
                                      status='ingebruik',
                                      definitie='De boom is aangeplant tussen 1980 en 2000.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKlassePlantjaar/1980-2000'),
        '2000-2020': KeuzelijstWaarde(invulwaarde='2000-2020',
                                      label='2000-2020',
                                      status='ingebruik',
                                      definitie='De boom is aangeplant tussen 2000 en 2020.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKlassePlantjaar/2000-2020'),
        '2020-2040': KeuzelijstWaarde(invulwaarde='2020-2040',
                                      label='2020-2040',
                                      status='ingebruik',
                                      definitie='De boom is aangeplant tussen 2020 en 2040.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKlassePlantjaar/2020-2040'),
        'ongekend': KeuzelijstWaarde(invulwaarde='ongekend',
                                     label='ongekend',
                                     status='ingebruik',
                                     definitie='Het is niet gekend wanneer de boom is aangeplant.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKlassePlantjaar/ongekend')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlKlassePlantjaar.get_dummy_data()

