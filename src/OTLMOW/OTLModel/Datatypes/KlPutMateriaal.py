# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPutMateriaal(KeuzelijstField):
    """Vervaardigingsmaterialen van de put."""
    naam = 'KlPutMateriaal'
    label = 'Put materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPutMateriaal'
    definition = 'Vervaardigingsmaterialen van de put.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPutMateriaal'
    options = {
        'PE-of-PP': KeuzelijstWaarde(invulwaarde='PE-of-PP',
                                     label='PE of PP',
                                     definitie='PE of PP',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutMateriaal/PE-of-PP'),
        'beton-of-gres': KeuzelijstWaarde(invulwaarde='beton-of-gres',
                                          label='beton of gres',
                                          definitie='beton of gres',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutMateriaal/beton-of-gres'),
        'beton-of-metselwerk': KeuzelijstWaarde(invulwaarde='beton-of-metselwerk',
                                                label='beton of metselwerk',
                                                definitie='beton of metselwerk',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutMateriaal/beton-of-metselwerk'),
        'glasvezelversterkt-polyesterhars': KeuzelijstWaarde(invulwaarde='glasvezelversterkt-polyesterhars',
                                                             label='glasvezelversterkt polyesterhars',
                                                             definitie='glasvezelversterkt polyesterhars',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutMateriaal/glasvezelversterkt-polyesterhars'),
        'ter-plaatse-gestort-beton': KeuzelijstWaarde(invulwaarde='ter-plaatse-gestort-beton',
                                                      label='ter plaatse gestort beton',
                                                      definitie='ter plaatse gestort beton',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutMateriaal/ter-plaatse-gestort-beton')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlPutMateriaal.get_dummy_data()

