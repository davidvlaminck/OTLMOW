# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOperationeleStatus(KeuzelijstField):
    """Operationele status codes."""
    naam = 'KlOperationeleStatus'
    label = 'Keuzelijst operationele status'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOperationeleStatus'
    definition = 'Operationele status codes.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOperationeleStatus'
    options = {
        'actief': KeuzelijstWaarde(invulwaarde='actief',
                                   label='actief',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOperationeleStatus/actief'),
        'actief-met-geplande-verwijdering': KeuzelijstWaarde(invulwaarde='actief-met-geplande-verwijdering',
                                                             label='actief met geplande verwijdering',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOperationeleStatus/actief-met-geplande-verwijdering'),
        'actief-met-geplande-wijziging': KeuzelijstWaarde(invulwaarde='actief-met-geplande-wijziging',
                                                          label='actief met geplande wijziging',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOperationeleStatus/actief-met-geplande-wijziging'),
        'actief-met-tijdelijke-wijziging': KeuzelijstWaarde(invulwaarde='actief-met-tijdelijke-wijziging',
                                                            label='actief met tijdelijke wijziging',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOperationeleStatus/actief-met-tijdelijke-wijziging'),
        'tijdelijk-actief': KeuzelijstWaarde(invulwaarde='tijdelijk-actief',
                                             label='tijdelijk actief',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOperationeleStatus/tijdelijk-actief'),
        'tijdelijk-inactief': KeuzelijstWaarde(invulwaarde='tijdelijk-inactief',
                                               label='tijdelijk inactief',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOperationeleStatus/tijdelijk-inactief')
    }

