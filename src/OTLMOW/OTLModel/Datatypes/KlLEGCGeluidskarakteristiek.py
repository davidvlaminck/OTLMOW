# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCGeluidskarakteristiek(KeuzelijstField):
    """De geluidskarakteristieken van de geluidswerende constructie."""
    naam = 'KlLEGCGeluidskarakteristiek'
    label = 'Geluidskarakteristiek'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCGeluidskarakteristiek'
    definition = 'De geluidskarakteristieken van de geluidswerende constructie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCGeluidskarakteristiek'
    options = {
        'absorberend': KeuzelijstWaarde(invulwaarde='absorberend',
                                        label='absorberend',
                                        status='ingebruik',
                                        definitie='De geluidsgolven worden gedeeltelijk niet weerkaatst door de geluidswerende constructie.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCGeluidskarakteristiek/absorberend'),
        'bi-absorberend': KeuzelijstWaarde(invulwaarde='bi-absorberend',
                                           label='bi-absorberend',
                                           status='ingebruik',
                                           definitie='De geluidsgolven worden gedeeltelijk niet weerkaatst door de geluidswerende constructie (langs beide zijden).',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCGeluidskarakteristiek/bi-absorberend'),
        'reflecterend': KeuzelijstWaarde(invulwaarde='reflecterend',
                                         label='reflecterend',
                                         status='ingebruik',
                                         definitie='reflecterend',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCGeluidskarakteristiek/reflecterend')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

