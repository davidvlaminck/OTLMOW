# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPictogramSymbool(KeuzelijstField):
    """De mogelijke symbolen op het pictogram."""
    naam = 'KlPictogramSymbool'
    label = 'Pictogram symbool'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPictogramSymbool'
    definition = 'De mogelijke symbolen op het pictogram.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPictogramSymbool'
    options = {
        'halte': KeuzelijstWaarde(invulwaarde='halte',
                                  label='halte',
                                  status='ingebruik',
                                  definitie='Duidt de locatie aan waar het openbaar vervoer, bv. bus, tram of trolley, stopt om passagiers te laten in- en uitstappen.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/halte'),
        'hydrant-bovengronds-(H)': KeuzelijstWaarde(invulwaarde='hydrant-bovengronds-(H)',
                                                    label='hydrant bovengronds (H)',
                                                    status='ingebruik',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/hydrant-bovengronds-(H)'),
        'hydrant-ondergronds-(B)': KeuzelijstWaarde(invulwaarde='hydrant-ondergronds-(B)',
                                                    label='hydrant ondergronds (B)',
                                                    status='ingebruik',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/hydrant-ondergronds-(B)'),
        'nooddeurnummer': KeuzelijstWaarde(invulwaarde='nooddeurnummer',
                                           label='nooddeurnummer',
                                           status='ingebruik',
                                           definitie='nooddeurnummer',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/nooddeurnummer'),
        'nummer-veiligheidsnis': KeuzelijstWaarde(invulwaarde='nummer-veiligheidsnis',
                                                  label='nummer veiligheidsnis',
                                                  status='ingebruik',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/nummer-veiligheidsnis'),
        'tunnelnaam': KeuzelijstWaarde(invulwaarde='tunnelnaam',
                                       label='tunnelnaam',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/tunnelnaam'),
        'verbodsbord': KeuzelijstWaarde(invulwaarde='verbodsbord',
                                        label='verbodsbord',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/verbodsbord'),
        'vluchtend-persoon': KeuzelijstWaarde(invulwaarde='vluchtend-persoon',
                                              label='vluchtend persoon',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/vluchtend-persoon')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlPictogramSymbool.get_dummy_data()

