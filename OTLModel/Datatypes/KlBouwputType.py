# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBouwputType(KeuzelijstField):
    """Het type van bouwput."""
    naam = 'KlBouwputType'
    label = 'Bouwput type.'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBouwputType'
    definition = 'Het type van bouwput.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBouwputType'
    options = {
        'bouwput': KeuzelijstWaarde(invulwaarde='bouwput',
                                    label='bouwput',
                                    definitie='bouwput',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBouwputType/bouwput'),
        'intredeput': KeuzelijstWaarde(invulwaarde='intredeput',
                                       label='intredeput',
                                       definitie='intredeput',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBouwputType/intredeput'),
        'ontvangstput': KeuzelijstWaarde(invulwaarde='ontvangstput',
                                         label='ontvangstput',
                                         definitie='ontvangstput',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBouwputType/ontvangstput'),
        'persput': KeuzelijstWaarde(invulwaarde='persput',
                                    label='persput',
                                    definitie='persput',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBouwputType/persput')
    }

