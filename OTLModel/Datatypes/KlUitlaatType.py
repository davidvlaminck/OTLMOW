# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUitlaatType(KeuzelijstField):
    """De verschillende types van uitlaat."""
    naam = 'KlUitlaatType'
    label = 'Uitlaat type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlUitlaatType'
    definition = 'De verschillende types van uitlaat.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUitlaatType'
    options = {
        'inlaat': KeuzelijstWaarde(invulwaarde='inlaat',
                                   label='inlaat',
                                   definitie='locatie waar water van een open profiel naar een inbuizing overgaat',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitlaatType/inlaat'),
        'uitlaat': KeuzelijstWaarde(invulwaarde='uitlaat',
                                    label='uitlaat',
                                    definitie='locatie waar water van een inbuizing naar een open profiel overgaat',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitlaatType/uitlaat')
    }

