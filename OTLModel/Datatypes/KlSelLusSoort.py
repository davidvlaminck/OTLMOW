# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSelLusSoort(KeuzelijstField):
    """Keuzelijst met verschillende soorten selectieve lussen."""
    naam = 'KlSelLusSoort'
    label = 'Selectieve lus soort'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSelLusSoort'
    definition = 'Keuzelijst met verschillende soorten selectieve lussen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSelLusSoort'
    options = {
        'buslus': KeuzelijstWaarde(invulwaarde='buslus',
                                   label='buslus',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusSoort/buslus'),
        'trambuslus': KeuzelijstWaarde(invulwaarde='trambuslus',
                                       label='trambuslus',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusSoort/trambuslus'),
        'trambuslus-virtueel': KeuzelijstWaarde(invulwaarde='trambuslus-virtueel',
                                                label='trambuslus virtueel',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusSoort/trambuslus-virtueel'),
        'tramlus': KeuzelijstWaarde(invulwaarde='tramlus',
                                    label='tramlus',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusSoort/tramlus'),
        'tramlus-magnetisch': KeuzelijstWaarde(invulwaarde='tramlus-magnetisch',
                                               label='tramlus magnetisch',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusSoort/tramlus-magnetisch'),
        'tramlus-virtueel': KeuzelijstWaarde(invulwaarde='tramlus-virtueel',
                                             label='tramlus virtueel',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusSoort/tramlus-virtueel'),
        'tramlus-wisselcontact-DeLijn': KeuzelijstWaarde(invulwaarde='tramlus-wisselcontact-DeLijn',
                                                         label='tramlus wisselcontact DeLijn',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusSoort/tramlus-wisselcontact-DeLijn')
    }

