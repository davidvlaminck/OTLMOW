# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDekselKaderType(KeuzelijstField):
    """Types van dekselkader."""
    naam = 'KlDekselKaderType'
    label = 'Dekselkader type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDekselKaderType'
    definition = 'Types van dekselkader.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDekselKaderType'
    options = {
        'enkelvoudig-gietijzeren-controleluik': KeuzelijstWaarde(invulwaarde='enkelvoudig-gietijzeren-controleluik',
                                                                 label='enkelvoudig gietijzeren controleluik',
                                                                 status='ingebruik',
                                                                 definitie='enkelvoudig gietijzeren controleluik',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKaderType/enkelvoudig-gietijzeren-controleluik'),
        'meerdelige-gietijzeren-controleluik': KeuzelijstWaarde(invulwaarde='meerdelige-gietijzeren-controleluik',
                                                                label='meerdelige gietijzeren controleluik',
                                                                status='ingebruik',
                                                                definitie='meerdelige gietijzeren controleluik',
                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKaderType/meerdelige-gietijzeren-controleluik'),
        'type-1': KeuzelijstWaarde(invulwaarde='type-1',
                                   label='type 1',
                                   status='ingebruik',
                                   definitie='type 1',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKaderType/type-1'),
        'type-2': KeuzelijstWaarde(invulwaarde='type-2',
                                   label='type 2',
                                   status='ingebruik',
                                   definitie='type 2',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKaderType/type-2'),
        'type-3': KeuzelijstWaarde(invulwaarde='type-3',
                                   label='type 3',
                                   status='ingebruik',
                                   definitie='type 3',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKaderType/type-3'),
        'type-4': KeuzelijstWaarde(invulwaarde='type-4',
                                   label='type 4',
                                   status='ingebruik',
                                   definitie='type 4',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKaderType/type-4'),
        'type-5': KeuzelijstWaarde(invulwaarde='type-5',
                                   label='type 5',
                                   status='ingebruik',
                                   definitie='type 5',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKaderType/type-5'),
        'type-6': KeuzelijstWaarde(invulwaarde='type-6',
                                   label='type 6',
                                   status='ingebruik',
                                   definitie='type 6',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKaderType/type-6'),
        'type-7': KeuzelijstWaarde(invulwaarde='type-7',
                                   label='type 7',
                                   status='ingebruik',
                                   definitie='type 7',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKaderType/type-7'),
        'type-8': KeuzelijstWaarde(invulwaarde='type-8',
                                   label='type 8',
                                   status='ingebruik',
                                   definitie='type 8',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKaderType/type-8'),
        'type-9': KeuzelijstWaarde(invulwaarde='type-9',
                                   label='type 9',
                                   status='ingebruik',
                                   definitie='type 9',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKaderType/type-9')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

