# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUitlaatType(KeuzelijstField):
    """De verschillende types van uitlaat."""
    naam = 'KlUitlaatType'
    label = 'Uitlaat type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlUitlaatType'
    definition = 'De verschillende types van uitlaat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUitlaatType'
    options = {
        'inlaat': KeuzelijstWaarde(invulwaarde='inlaat',
                                   label='inlaat',
                                   status='ingebruik',
                                   definitie='locatie waar water van een open profiel naar een inbuizing overgaat',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitlaatType/inlaat'),
        'uitlaat': KeuzelijstWaarde(invulwaarde='uitlaat',
                                    label='uitlaat',
                                    status='ingebruik',
                                    definitie='locatie waar water van een inbuizing naar een open profiel overgaat',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitlaatType/uitlaat')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

