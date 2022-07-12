# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDekselMateriaal(KeuzelijstField):
    """Het materiaal waaruit het deksel bestaat."""
    naam = 'KlDekselMateriaal'
    label = 'Dekselmateriaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDekselMateriaal'
    definition = 'Het materiaal waaruit het deksel bestaat.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDekselMateriaal'
    options = {
        'anders': KeuzelijstWaarde(invulwaarde='anders',
                                   label='anders',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='anders',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/anders'),
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='beton',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/beton'),
        'betonnen-segmenten': KeuzelijstWaarde(invulwaarde='betonnen-segmenten',
                                               label='betonnen segmenten',
                                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                               definitie='betonnen segmenten',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/betonnen-segmenten'),
        'cementmortel': KeuzelijstWaarde(invulwaarde='cementmortel',
                                         label='cementmortel',
                                         status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie='cementmortel',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/cementmortel'),
        'gewapend-beton': KeuzelijstWaarde(invulwaarde='gewapend-beton',
                                           label='gewapend beton',
                                           status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='gewapend beton',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/gewapend-beton'),
        'gietijzer': KeuzelijstWaarde(invulwaarde='gietijzer',
                                      label='gietijzer',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='nodulair gietijzer',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/gietijzer'),
        'grijs-gietijzer': KeuzelijstWaarde(invulwaarde='grijs-gietijzer',
                                            label='grijs gietijzer',
                                            status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            definitie='grijs gietijzer',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/grijs-gietijzer'),
        'ongeïdentificeerd-materiaal': KeuzelijstWaarde(invulwaarde='ongeïdentificeerd-materiaal',
                                                        label='ongeïdentificeerd materiaal',
                                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                        definitie='ongeïdentificeerd materiaal',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/ongeïdentificeerd-materiaal'),
        'ongeïdentificeerd-type-ijzer-of-staal': KeuzelijstWaarde(invulwaarde='ongeïdentificeerd-type-ijzer-of-staal',
                                                                  label='ongeïdentificeerd type ijzer of staal',
                                                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                  definitie='ongeïdentificeerd type ijzer of staal',
                                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/ongeïdentificeerd-type-ijzer-of-staal'),
        'ongeïdentificeerd-type-kunststof': KeuzelijstWaarde(invulwaarde='ongeïdentificeerd-type-kunststof',
                                                             label='ongeïdentificeerd type kunststof',
                                                             status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                             definitie='ongeïdentificeerd type kunststof',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/ongeïdentificeerd-type-kunststof'),
        'smeedijzer': KeuzelijstWaarde(invulwaarde='smeedijzer',
                                       label='smeedijzer',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='smeedijzer',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/smeedijzer'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='staal',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselMateriaal/staal')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlDekselMateriaal.get_dummy_data()

