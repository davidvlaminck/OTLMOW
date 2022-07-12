# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFiguratieCodeVerschuind(KeuzelijstField):
    """Codes voor de verschuinde figuratie markering."""
    naam = 'KlFiguratieCodeVerschuind'
    label = 'Figuratie code verschuind'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFiguratieCodeVerschuind'
    definition = 'Codes voor de verschuinde figuratie markering.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFiguratieCodeVerschuind'
    options = {
        'STOP-SmSc': KeuzelijstWaarde(invulwaarde='STOP-SmSc',
                                      label='STOP-SmSc',
                                      status='ingebruik',
                                      definitie='Een STOP markering smal en schuin.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCodeVerschuind/STOP-SmSc'),
        'VB-B1-GRsch': KeuzelijstWaarde(invulwaarde='VB-B1-GRsch',
                                        label='VB-B1-GRsch',
                                        status='ingebruik',
                                        definitie='Een omgekeerde driehoekmarkering groot en schuin.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCodeVerschuind/VB-B1-GRsch')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlFiguratieCodeVerschuind.get_dummy_data()

