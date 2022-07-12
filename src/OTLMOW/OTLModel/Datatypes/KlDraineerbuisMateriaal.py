# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDraineerbuisMateriaal(KeuzelijstField):
    """Materialen van de draineerbuis."""
    naam = 'KlDraineerbuisMateriaal'
    label = 'Draineerbuis materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDraineerbuisMateriaal'
    definition = 'Materialen van de draineerbuis.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDraineerbuisMateriaal'
    options = {
        'draineerbuizen-van-beton-volgens-3-26.1.5': KeuzelijstWaarde(invulwaarde='draineerbuizen-van-beton-volgens-3-26.1.5',
                                                                      label='draineerbuizen van beton volgens 3-26.1.5',
                                                                      status='ingebruik',
                                                                      definitie='draineerbuizen van beton volgens 3-26.1.5',
                                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraineerbuisMateriaal/draineerbuizen-van-beton-volgens-3-26.1.5'),
        'draineerbuizen-van-gres-volgens-3-26.1.4': KeuzelijstWaarde(invulwaarde='draineerbuizen-van-gres-volgens-3-26.1.4',
                                                                     label='draineerbuizen van gres volgens 3-26.1.4',
                                                                     status='ingebruik',
                                                                     definitie='draineerbuizen van gres volgens 3-26.1.4',
                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraineerbuisMateriaal/draineerbuizen-van-gres-volgens-3-26.1.4'),
        'draineerbuizen-van-polyethyleen-volgens-3-26.1.2': KeuzelijstWaarde(invulwaarde='draineerbuizen-van-polyethyleen-volgens-3-26.1.2',
                                                                             label='draineerbuizen van polyethyleen volgens 3-26.1.2',
                                                                             status='ingebruik',
                                                                             definitie='draineerbuizen van polyethyleen volgens 3-26.1.2',
                                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraineerbuisMateriaal/draineerbuizen-van-polyethyleen-volgens-3-26.1.2'),
        'draineerbuizen-van-profielversterkte-HDPE-volgens-3-26.1.6': KeuzelijstWaarde(invulwaarde='draineerbuizen-van-profielversterkte-HDPE-volgens-3-26.1.6',
                                                                                       label='draineerbuizen van profielversterkte HDPE volgens 3-26.1.6',
                                                                                       status='ingebruik',
                                                                                       definitie='draineerbuizen van profielversterkte HDPE volgens 3-26.1.6',
                                                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraineerbuisMateriaal/draineerbuizen-van-profielversterkte-HDPE-volgens-3-26.1.6'),
        'geribbelde-draineerbuizen-van-PVC-met-kous-volgens-3-26.1.1': KeuzelijstWaarde(invulwaarde='geribbelde-draineerbuizen-van-PVC-met-kous-volgens-3-26.1.1',
                                                                                        label='geribbelde draineerbuizen van PVC met kous volgens 3-26.1.1',
                                                                                        status='ingebruik',
                                                                                        definitie='geribbelde draineerbuizen van PVC met kous volgens 3-26.1.1',
                                                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraineerbuisMateriaal/geribbelde-draineerbuizen-van-PVC-met-kous-volgens-3-26.1.1'),
        'geribbelde-draineerbuizen-van-PVC-zonder-kous-volgens-3-26.1.1': KeuzelijstWaarde(invulwaarde='geribbelde-draineerbuizen-van-PVC-zonder-kous-volgens-3-26.1.1',
                                                                                           label='geribbelde draineerbuizen van PVC zonder kous volgens 3-26.1.1',
                                                                                           status='ingebruik',
                                                                                           definitie='geribbelde draineerbuizen van PVC zonder kous volgens 3-26.1.1',
                                                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraineerbuisMateriaal/geribbelde-draineerbuizen-van-PVC-zonder-kous-volgens-3-26.1.1')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlDraineerbuisMateriaal.get_dummy_data()

