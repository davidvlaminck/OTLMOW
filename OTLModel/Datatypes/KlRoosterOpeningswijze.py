# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRoosterOpeningswijze(KeuzelijstField):
    """Deze keuzelijst geeft de manier aan hoe het rooster geopend kan worden."""
    naam = 'KlRoosterOpeningswijze'
    label = 'Rooster openingswijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRoosterOpeningswijze'
    definition = 'Deze keuzelijst geeft de manier aan hoe het rooster geopend kan worden.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRoosterOpeningswijze'
    options = {
        'ovaal-deksel': KeuzelijstWaarde(invulwaarde='ovaal-deksel',
                                         label='ovaal deksel',
                                         definitie='ovaal deksel',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRoosterOpeningswijze/ovaal-deksel'),
        'scharnierend': KeuzelijstWaarde(invulwaarde='scharnierend',
                                         label='scharnierend',
                                         definitie='scharnierend',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRoosterOpeningswijze/scharnierend'),
        'uitneembaar': KeuzelijstWaarde(invulwaarde='uitneembaar',
                                        label='uitneembaar',
                                        definitie='uitneembaar',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRoosterOpeningswijze/uitneembaar')
    }

