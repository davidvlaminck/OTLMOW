# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSteenslagType(KeuzelijstField):
    """Steenslag types."""
    naam = 'KlSteenslagType'
    label = 'Steenslag type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSteenslagType'
    definition = 'Steenslag types.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSteenslagType'
    options = {
        'type-IA': KeuzelijstWaarde(invulwaarde='type-IA',
                                    label='type IA',
                                    definitie='type IA',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IA'),
        'type-IB': KeuzelijstWaarde(invulwaarde='type-IB',
                                    label='type IB',
                                    definitie='type IB',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IB'),
        'type-IIA': KeuzelijstWaarde(invulwaarde='type-IIA',
                                     label='type IIA',
                                     definitie='type IIA',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IIA'),
        'type-IIB': KeuzelijstWaarde(invulwaarde='type-IIB',
                                     label='type IIB',
                                     definitie='type IIB',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IIB'),
        'type-IIIA': KeuzelijstWaarde(invulwaarde='type-IIIA',
                                      label='type IIIA',
                                      definitie='type IIIA',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IIIA'),
        'type-IIIB': KeuzelijstWaarde(invulwaarde='type-IIIB',
                                      label='type IIIB',
                                      definitie='type IIIB',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IIIB')
    }

