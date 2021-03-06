# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlControllerBeveiligingssleutel(KeuzelijstField):
    """De encryptie die wordt toegepast om de verbinding tussen lokaal en centraal te beveiligen."""
    naam = 'KlControllerBeveiligingssleutel'
    label = 'Controller beveiligingssleutel.'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlControllerBeveiligingssleutel'
    definition = 'De encryptie die wordt toegepast om de verbinding tussen lokaal en centraal te beveiligen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlControllerBeveiligingssleutel'
    options = {
        'AES-256': KeuzelijstWaarde(invulwaarde='AES-256',
                                    label='AES-256',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlControllerBeveiligingssleutel/AES-256')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

