# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSchanskorfVorm(KeuzelijstField):
    """Vormen van schanskorven."""
    naam = 'KlSchanskorfVorm'
    label = 'Schanskorf vorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSchanskorfVorm'
    definition = 'Vormen van schanskorven.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSchanskorfVorm'
    options = {
        'in-blokvorm': KeuzelijstWaarde(invulwaarde='in-blokvorm',
                                        label='in blokvorm',
                                        status='ingebruik',
                                        definitie='in blokvorm',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchanskorfVorm/in-blokvorm'),
        'in-matrasvorm': KeuzelijstWaarde(invulwaarde='in-matrasvorm',
                                          label='in matrasvorm',
                                          status='ingebruik',
                                          definitie='in matrasvorm',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchanskorfVorm/in-matrasvorm')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlSchanskorfVorm.get_dummy_data()

