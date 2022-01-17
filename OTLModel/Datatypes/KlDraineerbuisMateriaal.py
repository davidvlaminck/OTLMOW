# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDraineerbuisMateriaal(KeuzelijstField):
    """Materialen van de draineerbuis."""
    naam = 'KlDraineerbuisMateriaal'
    label = 'Draineerbuis materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDraineerbuisMateriaal'
    definition = 'Materialen van de draineerbuis.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDraineerbuisMateriaal'
    options = {
        'draineerbuizen-van-beton-volgens-3-26.1.5': KeuzelijstWaarde(invulwaarde='draineerbuizen-van-beton-volgens-3-26.1.5',
                                                                      label='draineerbuizen van beton volgens 3-26.1.5',
                                                                      definitie='draineerbuizen van beton volgens 3-26.1.5',
                                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraineerbuisMateriaal/draineerbuizen-van-beton-volgens-3-26.1.5'),
        'draineerbuizen-van-gres-volgens-3-26.1.4': KeuzelijstWaarde(invulwaarde='draineerbuizen-van-gres-volgens-3-26.1.4',
                                                                     label='draineerbuizen van gres volgens 3-26.1.4',
                                                                     definitie='draineerbuizen van gres volgens 3-26.1.4',
                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraineerbuisMateriaal/draineerbuizen-van-gres-volgens-3-26.1.4'),
        'draineerbuizen-van-polyethyleen-volgens-3-26.1.2': KeuzelijstWaarde(invulwaarde='draineerbuizen-van-polyethyleen-volgens-3-26.1.2',
                                                                             label='draineerbuizen van polyethyleen volgens 3-26.1.2',
                                                                             definitie='draineerbuizen van polyethyleen volgens 3-26.1.2',
                                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraineerbuisMateriaal/draineerbuizen-van-polyethyleen-volgens-3-26.1.2'),
        'draineerbuizen-van-profielversterkte-HDPE-volgens-3-26.1.6': KeuzelijstWaarde(invulwaarde='draineerbuizen-van-profielversterkte-HDPE-volgens-3-26.1.6',
                                                                                       label='draineerbuizen van profielversterkte HDPE volgens 3-26.1.6',
                                                                                       definitie='draineerbuizen van profielversterkte HDPE volgens 3-26.1.6',
                                                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraineerbuisMateriaal/draineerbuizen-van-profielversterkte-HDPE-volgens-3-26.1.6'),
        'geribbelde-draineerbuizen-van-PVC-met-kous-volgens-3-26.1.1': KeuzelijstWaarde(invulwaarde='geribbelde-draineerbuizen-van-PVC-met-kous-volgens-3-26.1.1',
                                                                                        label='geribbelde draineerbuizen van PVC met kous volgens 3-26.1.1',
                                                                                        definitie='geribbelde draineerbuizen van PVC met kous volgens 3-26.1.1',
                                                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraineerbuisMateriaal/geribbelde-draineerbuizen-van-PVC-met-kous-volgens-3-26.1.1'),
        'geribbelde-draineerbuizen-van-PVC-zonder-kous-volgens-3-26.1.1': KeuzelijstWaarde(invulwaarde='geribbelde-draineerbuizen-van-PVC-zonder-kous-volgens-3-26.1.1',
                                                                                           label='geribbelde draineerbuizen van PVC zonder kous volgens 3-26.1.1',
                                                                                           definitie='geribbelde draineerbuizen van PVC zonder kous volgens 3-26.1.1',
                                                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraineerbuisMateriaal/geribbelde-draineerbuizen-van-PVC-zonder-kous-volgens-3-26.1.1')
    }

