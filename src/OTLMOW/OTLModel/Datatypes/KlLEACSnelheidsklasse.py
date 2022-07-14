# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACSnelheidsklasse(KeuzelijstField):
    """De verschillende snelheidsklasses van afschermende constructies."""
    naam = 'KlLEACSnelheidsklasse'
    label = 'Snelheidsklasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACSnelheidsklasse'
    definition = 'De verschillende snelheidsklasses van afschermende constructies.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACSnelheidsklasse'
    options = {
        'C60': KeuzelijstWaarde(invulwaarde='C60',
                                label='C60',
                                status='ingebruik',
                                definitie='Getest bij 60 km/h',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACSnelheidsklasse/C60'),
        'C70': KeuzelijstWaarde(invulwaarde='C70',
                                label='C70',
                                status='ingebruik',
                                definitie='Getest bij 70 km/h',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACSnelheidsklasse/C70')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

