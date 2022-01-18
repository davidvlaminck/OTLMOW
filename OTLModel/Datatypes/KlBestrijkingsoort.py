# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBestrijkingsoort(KeuzelijstField):
    """Soorten van bestrijking."""
    naam = 'KlBestrijkingsoort'
    label = 'Bestrijkingsoort'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBestrijkingsoort'
    definition = 'Soorten van bestrijking.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBestrijkingsoort'
    options = {
        'eenlaagse-met-dubbele-begrinding-(EBDB)': KeuzelijstWaarde(invulwaarde='eenlaagse-met-dubbele-begrinding-(EBDB)',
                                                                    label='eenlaagse met dubbele begrinding (EBDB)',
                                                                    definitie='éénlaagse bestrijking met dubbele begrinding (EBDB)',
                                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingsoort/eenlaagse-met-dubbele-begrinding-(EBDB)'),
        'eenlaagse-met-enkele-begrinding-(EBEB)': KeuzelijstWaarde(invulwaarde='eenlaagse-met-enkele-begrinding-(EBEB)',
                                                                   label='eenlaagse met enkele begrinding (EBEB)',
                                                                   definitie='éénlaagse bestrijking met enkele begrinding (EBEB)',
                                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingsoort/eenlaagse-met-enkele-begrinding-(EBEB)'),
        'tweelaagse-(TB)': KeuzelijstWaarde(invulwaarde='tweelaagse-(TB)',
                                            label='tweelaagse (TB)',
                                            definitie='tweelaagse bestrijking (TB)',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingsoort/tweelaagse-(TB)')
    }

