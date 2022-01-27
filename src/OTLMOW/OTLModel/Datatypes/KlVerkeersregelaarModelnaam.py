# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersregelaarModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor Verkeersregelaar."""
    naam = 'KlVerkeersregelaarModelnaam'
    label = 'verkeersregelaar modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersregelaarModelnaam'
    definition = 'Keuzelijst met modelnamen voor Verkeersregelaar.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersregelaarModelnaam'
    options = {
        'civa-2020': KeuzelijstWaarde(invulwaarde='civa-2020',
                                      label='CIVA 2020',
                                      definitie='CIVA 2020',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarModelnaam/civa-2020'),
        'flow-node': KeuzelijstWaarde(invulwaarde='flow-node',
                                      label='FlowNode',
                                      definitie='FlowNode',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarModelnaam/flow-node')
    }

