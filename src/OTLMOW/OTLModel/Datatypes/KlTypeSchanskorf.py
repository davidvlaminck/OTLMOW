# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeSchanskorf(KeuzelijstField):
    """Keuzelijst met de verschillende types schanskorven."""
    naam = 'KlTypeSchanskorf'
    label = 'Type schanskorf'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeSchanskorf'
    definition = 'Keuzelijst met de verschillende types schanskorven.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeSchanskorf'
    options = {
        '5-x-7': KeuzelijstWaarde(invulwaarde='5-x-7',
                                  label='5 x 7',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeSchanskorf/5-x-7'),
        '6-x-8': KeuzelijstWaarde(invulwaarde='6-x-8',
                                  label='6 x 8',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeSchanskorf/6-x-8')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

