# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIOSignaaltype(KeuzelijstField):
    """Geeft aan of de IO-kaart werkt met een digitaal of met een analoog signaal."""
    naam = 'KlIOSignaaltype'
    label = 'IO-kaart signaaltype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIOSignaaltype'
    definition = 'Geeft aan of de IO-kaart werkt met een digitaal of met een analoog signaal.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIOSignaaltype'
    options = {
        'analoog': KeuzelijstWaarde(invulwaarde='analoog',
                                    label='analoog',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOSignaaltype/analoog'),
        'digitaal': KeuzelijstWaarde(invulwaarde='digitaal',
                                     label='digitaal',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOSignaaltype/digitaal')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

