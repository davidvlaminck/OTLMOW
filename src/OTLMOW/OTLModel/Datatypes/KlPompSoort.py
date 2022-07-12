# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPompSoort(KeuzelijstField):
    """Soorten pomp."""
    naam = 'KlPompSoort'
    label = 'Pomp soort'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPompSoort'
    definition = 'Soorten pomp.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPompSoort'
    options = {
        'LPR-pomp-(luchtpersriolering)': KeuzelijstWaarde(invulwaarde='LPR-pomp-(luchtpersriolering)',
                                                          label='LPR-pomp (luchtpersriolering)',
                                                          status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                          definitie='LPR-pomp (luchtpersriolering)',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPompSoort/LPR-pomp-(luchtpersriolering)'),
        'dompelpomp': KeuzelijstWaarde(invulwaarde='dompelpomp',
                                       label='dompelpomp',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='dompelpomp',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPompSoort/dompelpomp'),
        'radiale-centrifugaalpomp-(dompel)': KeuzelijstWaarde(invulwaarde='radiale-centrifugaalpomp-(dompel)',
                                                              label='radiale centrifugaalpomp (dompel)',
                                                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                              definitie='Radiale centrifugaalpomp (dompel)',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPompSoort/radiale-centrifugaalpomp-(dompel)'),
        'radiale-centrifugaalpomp-(droog)': KeuzelijstWaarde(invulwaarde='radiale-centrifugaalpomp-(droog)',
                                                             label='radiale centrifugaalpomp (droog)',
                                                             status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                             definitie='Radiale centrifugaalpomp (droog)',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPompSoort/radiale-centrifugaalpomp-(droog)'),
        'schachtpomp': KeuzelijstWaarde(invulwaarde='schachtpomp',
                                        label='schachtpomp',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='Schachtpomp',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPompSoort/schachtpomp'),
        'vijzelpomp': KeuzelijstWaarde(invulwaarde='vijzelpomp',
                                       label='vijzelpomp',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Vijzelpomp',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPompSoort/vijzelpomp')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlPompSoort.get_dummy_data()

