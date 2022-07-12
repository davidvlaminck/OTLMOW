# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHechtspecie(KeuzelijstField):
    """Keuzelijst met hecht specie van gestapelde ruwe steen."""
    naam = 'KlHechtspecie'
    label = 'Hecht specie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHechtspecie'
    definition = 'Keuzelijst met hecht specie van gestapelde ruwe steen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHechtspecie'
    options = {
        'gebiedseigen-grond': KeuzelijstWaarde(invulwaarde='gebiedseigen-grond',
                                               label='gebiedseigen grond',
                                               status='ingebruik',
                                               definitie='gebiedseigen grond',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHechtspecie/gebiedseigen-grond'),
        'zandcement': KeuzelijstWaarde(invulwaarde='zandcement',
                                       label='zandcement',
                                       status='ingebruik',
                                       definitie='zandcement',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHechtspecie/zandcement')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlHechtspecie.get_dummy_data()

