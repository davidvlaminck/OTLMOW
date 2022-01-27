# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSelLusVerbinding(KeuzelijstField):
    """Keuzelijst met soorten verbindingen voor selectieve lussen."""
    naam = 'KlSelLusVerbinding'
    label = 'Selectieve lus verbinding'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSelLusVerbinding'
    definition = 'Keuzelijst met soorten verbindingen voor selectieve lussen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSelLusVerbinding'
    options = {
        'contact': KeuzelijstWaarde(invulwaarde='contact',
                                    label='contact',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusVerbinding/contact'),
        'serieel': KeuzelijstWaarde(invulwaarde='serieel',
                                    label='serieel',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusVerbinding/serieel')
    }

