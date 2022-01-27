# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlContactpuntType(KeuzelijstField):
    """Keuzelijst voor types van deurcontacten volgens de gebruikte techniek."""
    naam = 'KlContactpuntType'
    label = 'Contactpunt type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlContactpuntType'
    definition = 'Keuzelijst voor types van deurcontacten volgens de gebruikte techniek.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlContactpuntType'
    options = {
        'deurcontact': KeuzelijstWaarde(invulwaarde='deurcontact',
                                        label='deurcontact',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlContactpuntType/deurcontact'),
        'magneetcontact': KeuzelijstWaarde(invulwaarde='magneetcontact',
                                           label='magneetcontact',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlContactpuntType/magneetcontact')
    }

