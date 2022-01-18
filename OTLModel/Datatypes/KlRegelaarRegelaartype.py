# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRegelaarRegelaartype(KeuzelijstField):
    """Keuzelijst met verschillende types verkeersregelaars."""
    naam = 'KlRegelaarRegelaartype'
    label = 'Regelaar regelaartype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRegelaarRegelaartype'
    definition = 'Keuzelijst met verschillende types verkeersregelaars.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRegelaarRegelaartype'
    options = {
        'type-0': KeuzelijstWaarde(invulwaarde='type-0',
                                   label='type 0',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRegelaarRegelaartype/type-0'),
        'type-1': KeuzelijstWaarde(invulwaarde='type-1',
                                   label='type 1',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRegelaarRegelaartype/type-1'),
        'type-2': KeuzelijstWaarde(invulwaarde='type-2',
                                   label='type 2',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRegelaarRegelaartype/type-2'),
        'type-3': KeuzelijstWaarde(invulwaarde='type-3',
                                   label='type 3',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRegelaarRegelaartype/type-3')
    }

