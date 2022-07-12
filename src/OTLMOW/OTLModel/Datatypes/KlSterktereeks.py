# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSterktereeks(KeuzelijstField):
    """De stabiliteitklasse van de buis."""
    naam = 'KlSterktereeks'
    label = 'Sterktereeks'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSterktereeks'
    definition = 'De stabiliteitklasse van de buis.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSterktereeks'
    options = {
        'GVP-SN10000-N-M2': KeuzelijstWaarde(invulwaarde='GVP-SN10000-N-M2',
                                             label='GVP SN10000 N/M2',
                                             status='ingebruik',
                                             definitie='GVP SN10000 N/M2',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterktereeks/GVP-SN10000-N-M2'),
        'GVP-SN2500-N-M2': KeuzelijstWaarde(invulwaarde='GVP-SN2500-N-M2',
                                            label='GVP SN2500 N/M2',
                                            status='ingebruik',
                                            definitie='GVP SN2500 N/M2',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterktereeks/GVP-SN2500-N-M2'),
        'GVP-SN5000-N-M2': KeuzelijstWaarde(invulwaarde='GVP-SN5000-N-M2',
                                            label='GVP SN5000 N/M2',
                                            status='ingebruik',
                                            definitie='GVP SN5000 N/M2',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterktereeks/GVP-SN5000-N-M2'),
        'PVC-SN16': KeuzelijstWaarde(invulwaarde='PVC-SN16',
                                     label='PVC SN16',
                                     status='ingebruik',
                                     definitie='PVC SN16',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterktereeks/PVC-SN16'),
        'PVC-SN2': KeuzelijstWaarde(invulwaarde='PVC-SN2',
                                    label='PVC SN2',
                                    status='ingebruik',
                                    definitie='PVC SN2',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterktereeks/PVC-SN2'),
        'PVC-SN4': KeuzelijstWaarde(invulwaarde='PVC-SN4',
                                    label='PVC SN4',
                                    status='ingebruik',
                                    definitie='PVC SN4',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterktereeks/PVC-SN4'),
        'PVC-SN8': KeuzelijstWaarde(invulwaarde='PVC-SN8',
                                    label='PVC SN8',
                                    status='ingebruik',
                                    definitie='PVC SN8',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterktereeks/PVC-SN8'),
        'gres-120': KeuzelijstWaarde(invulwaarde='gres-120',
                                     label='gres 120',
                                     status='ingebruik',
                                     definitie='gres 120',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterktereeks/gres-120'),
        'gres-160': KeuzelijstWaarde(invulwaarde='gres-160',
                                     label='gres 160',
                                     status='ingebruik',
                                     definitie='gres 160',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterktereeks/gres-160'),
        'gres-200': KeuzelijstWaarde(invulwaarde='gres-200',
                                     label='gres 200',
                                     status='ingebruik',
                                     definitie='gres 200',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterktereeks/gres-200'),
        'gres-240': KeuzelijstWaarde(invulwaarde='gres-240',
                                     label='gres 240',
                                     status='ingebruik',
                                     definitie='gres 240',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterktereeks/gres-240'),
        'gres-34': KeuzelijstWaarde(invulwaarde='gres-34',
                                    label='gres 34',
                                    status='ingebruik',
                                    definitie='gres 34',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterktereeks/gres-34'),
        'gres-95': KeuzelijstWaarde(invulwaarde='gres-95',
                                    label='gres 95',
                                    status='ingebruik',
                                    definitie='gres 95',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterktereeks/gres-95'),
        'gres-minimum-kruindrukwaarde-34': KeuzelijstWaarde(invulwaarde='gres-minimum-kruindrukwaarde-34',
                                                            label='gres minimum kruindrukwaarde 34',
                                                            status='ingebruik',
                                                            definitie='gres minimum kruindrukwaarde 34',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterktereeks/gres-minimum-kruindrukwaarde-34'),
        'gres-minimum-kruindrukwaarde-90': KeuzelijstWaarde(invulwaarde='gres-minimum-kruindrukwaarde-90',
                                                            label='gres minimum kruindrukwaarde 90',
                                                            status='ingebruik',
                                                            definitie='gres minimum kruindrukwaarde 90',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterktereeks/gres-minimum-kruindrukwaarde-90'),
        'hdpe-p-n-10': KeuzelijstWaarde(invulwaarde='hdpe-p-n-10',
                                        label='HDPE PN10',
                                        status='ingebruik',
                                        definitie='HDPE PN10',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterktereeks/hdpe-p-n-10'),
        'hdpe-p-n-16': KeuzelijstWaarde(invulwaarde='hdpe-p-n-16',
                                        label='HDPE PN16',
                                        status='ingebruik',
                                        definitie='HDPE PN16',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterktereeks/hdpe-p-n-16'),
        'pp-s-n-8': KeuzelijstWaarde(invulwaarde='pp-s-n-8',
                                     label='PP SN8',
                                     status='ingebruik',
                                     definitie='PP SN8',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterktereeks/pp-s-n-8'),
        'pvc-composiet-s-n-4': KeuzelijstWaarde(invulwaarde='pvc-composiet-s-n-4',
                                                label='PVC composiet SN4',
                                                status='ingebruik',
                                                definitie='PVC composiet SN4',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterktereeks/pvc-composiet-s-n-4'),
        'pvc-composiet-s-n-8': KeuzelijstWaarde(invulwaarde='pvc-composiet-s-n-8',
                                                label='PVC composiet SN8',
                                                status='ingebruik',
                                                definitie='PVC composiet SN8',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterktereeks/pvc-composiet-s-n-8')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlSterktereeks.get_dummy_data()

