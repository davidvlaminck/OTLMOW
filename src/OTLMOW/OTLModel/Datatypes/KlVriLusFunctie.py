# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVriLusFunctie(KeuzelijstField):
    """Keuzelijst met verschillende types detectielussen naar functie."""
    naam = 'KlVriLusFunctie'
    label = 'VRI-lus functie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVriLusFunctie'
    definition = 'Keuzelijst met verschillende types detectielussen naar functie.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVriLusFunctie'
    options = {
        'KAR-inmeldlus': KeuzelijstWaarde(invulwaarde='KAR-inmeldlus',
                                          label='KAR inmeldlus',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/KAR-inmeldlus'),
        'KAR-uitmeldlus': KeuzelijstWaarde(invulwaarde='KAR-uitmeldlus',
                                           label='KAR uitmeldlus',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/KAR-uitmeldlus'),
        'afstandslus': KeuzelijstWaarde(invulwaarde='afstandslus',
                                        label='afstandslus',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/afstandslus'),
        'filelus': KeuzelijstWaarde(invulwaarde='filelus',
                                    label='filelus',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/filelus'),
        'hiaatlus': KeuzelijstWaarde(invulwaarde='hiaatlus',
                                     label='hiaatlus',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/hiaatlus'),
        'stopstreeplus': KeuzelijstWaarde(invulwaarde='stopstreeplus',
                                          label='stopstreeplus',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/stopstreeplus')
    }

