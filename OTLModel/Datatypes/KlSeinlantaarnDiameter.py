# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSeinlantaarnDiameter(KeuzelijstField):
    """Keuzelijst met de verschillende voorkomende diameter-waarden voor Seinlantaarn."""
    naam = 'KlSeinlantaarnDiameter'
    label = 'Seinlantaarn diameter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlSeinlantaarnDiameter'
    definition = 'Keuzelijst met de verschillende voorkomende diameter-waarden voor Seinlantaarn.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSeinlantaarnDiameter'
    options = {
        '100': KeuzelijstWaarde(invulwaarde='100',
                                label='100',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinlantaarnDiameter/100'),
        '200': KeuzelijstWaarde(invulwaarde='200',
                                label='200',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinlantaarnDiameter/200'),
        '300': KeuzelijstWaarde(invulwaarde='300',
                                label='300',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinlantaarnDiameter/300')
    }

