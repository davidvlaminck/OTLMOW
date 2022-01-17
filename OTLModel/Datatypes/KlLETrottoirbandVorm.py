# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLETrottoirbandVorm(KeuzelijstField):
    """De vormen van een trottoirband."""
    naam = 'KlLETrottoirbandVorm'
    label = 'Trottoirband vorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLETrottoirbandVorm'
    definition = 'De vormen van een trottoirband.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLETrottoirbandVorm'
    options = {
        'afgeschuind': KeuzelijstWaarde(invulwaarde='afgeschuind',
                                        label='afgeschuind',
                                        definitie='Afgeschuind',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandVorm/afgeschuind')
    }

