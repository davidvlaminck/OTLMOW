# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPictogramSymbool(KeuzelijstField):
    """De mogelijke symbolen op het pictogram."""
    naam = 'KlPictogramSymbool'
    label = 'Pictogram symbool'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPictogramSymbool'
    definition = 'De mogelijke symbolen op het pictogram.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPictogramSymbool'
    options = {
        'halte': KeuzelijstWaarde(invulwaarde='halte',
                                  label='halte',
                                  definitie='Duidt de locatie aan waar het openbaar vervoer, bv. bus, tram of trolley, stopt om passagiers te laten in- en uitstappen.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/halte'),
        'hydrant-bovengronds-(H)': KeuzelijstWaarde(invulwaarde='hydrant-bovengronds-(H)',
                                                    label='hydrant bovengronds (H)',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/hydrant-bovengronds-(H)'),
        'hydrant-ondergronds-(B)': KeuzelijstWaarde(invulwaarde='hydrant-ondergronds-(B)',
                                                    label='hydrant ondergronds (B)',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/hydrant-ondergronds-(B)'),
        'nooddeurnummer': KeuzelijstWaarde(invulwaarde='nooddeurnummer',
                                           label='nooddeurnummer',
                                           definitie='nooddeurnummer',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/nooddeurnummer'),
        'nummer-veiligheidsnis': KeuzelijstWaarde(invulwaarde='nummer-veiligheidsnis',
                                                  label='nummer veiligheidsnis',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/nummer-veiligheidsnis'),
        'tunnelnaam': KeuzelijstWaarde(invulwaarde='tunnelnaam',
                                       label='tunnelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/tunnelnaam'),
        'verbodsbord': KeuzelijstWaarde(invulwaarde='verbodsbord',
                                        label='verbodsbord',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/verbodsbord'),
        'vluchtend-persoon': KeuzelijstWaarde(invulwaarde='vluchtend-persoon',
                                              label='vluchtend persoon',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/vluchtend-persoon')
    }

