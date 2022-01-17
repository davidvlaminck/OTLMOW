# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIORichting(KeuzelijstField):
    """Geeft aan of de IO-kaart dient voor input of output."""
    naam = 'KlIORichting'
    label = 'IO richting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIORichting'
    definition = 'Geeft aan of de IO-kaart dient voor input of output.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIORichting'
    options = {
        'input': KeuzelijstWaarde(invulwaarde='input',
                                  label='input',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIORichting/input'),
        'output': KeuzelijstWaarde(invulwaarde='output',
                                   label='output',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIORichting/output')
    }

