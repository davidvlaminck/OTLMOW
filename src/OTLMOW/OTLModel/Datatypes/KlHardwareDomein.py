# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHardwareDomein(KeuzelijstField):
    """Lijst met gebruikte administratieve groeperingen van meerdere particuliere computernetwerken of hosts binnen dezelfde infrastructuur."""
    naam = 'KlHardwareDomein'
    label = 'Hardware domein'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlHardwareDomein'
    definition = 'Lijst met gebruikte administratieve groeperingen van meerdere particuliere computernetwerken of hosts binnen dezelfde infrastructuur.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHardwareDomein'
    options = {
        'alfa': KeuzelijstWaarde(invulwaarde='alfa',
                                 label='alfa',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareDomein/alfa'),
        'belfla': KeuzelijstWaarde(invulwaarde='belfla',
                                   label='belfla',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareDomein/belfla')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

