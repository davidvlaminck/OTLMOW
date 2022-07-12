# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKleurMarkering(KeuzelijstField):
    """De mogeglijke markeringskleuren."""
    naam = 'KlKleurMarkering'
    label = 'Kleur markering'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKleurMarkering'
    definition = 'De mogeglijke markeringskleuren.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKleurMarkering'
    options = {
        'geel-(Y1)': KeuzelijstWaarde(invulwaarde='geel-(Y1)',
                                      label='geel (Y1)',
                                      status='ingebruik',
                                      definitie='Geel (Y1) als kleur van de markering.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurMarkering/geel-(Y1)'),
        'geel-(Y2)': KeuzelijstWaarde(invulwaarde='geel-(Y2)',
                                      label='geel (Y2)',
                                      status='ingebruik',
                                      definitie='Geel (Y2) als kleur van de markering.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurMarkering/geel-(Y2)'),
        'oker-(RAL1024)': KeuzelijstWaarde(invulwaarde='oker-(RAL1024)',
                                           label='oker (RAL1024)',
                                           status='ingebruik',
                                           definitie='Oker als de kleur van de markering.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurMarkering/oker-(RAL1024)'),
        'rood-(RAL3020)': KeuzelijstWaarde(invulwaarde='rood-(RAL3020)',
                                           label='rood (RAL3020)',
                                           status='ingebruik',
                                           definitie='Rood als de kleur van de markering.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurMarkering/rood-(RAL3020)'),
        'wit': KeuzelijstWaarde(invulwaarde='wit',
                                label='wit',
                                status='ingebruik',
                                definitie='Wit als de kleur van de markering.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurMarkering/wit')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlKleurMarkering.get_dummy_data()

