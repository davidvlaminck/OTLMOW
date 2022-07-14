# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlContactpuntType(KeuzelijstField):
    """Keuzelijst voor types van deurcontacten volgens de gebruikte techniek."""
    naam = 'KlContactpuntType'
    label = 'Contactpunt type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlContactpuntType'
    definition = 'Keuzelijst voor types van deurcontacten volgens de gebruikte techniek.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlContactpuntType'
    options = {
        'deurcontact': KeuzelijstWaarde(invulwaarde='deurcontact',
                                        label='deurcontact',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlContactpuntType/deurcontact'),
        'magneetcontact': KeuzelijstWaarde(invulwaarde='magneetcontact',
                                           label='magneetcontact',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlContactpuntType/magneetcontact')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

