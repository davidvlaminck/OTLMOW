# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACObstakelbeveiligerType(KeuzelijstField):
    """De verschillende types van obstakelbeveiliger."""
    naam = 'KlLEACObstakelbeveiligerType'
    label = 'Obstakelbeveiliger type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACObstakelbeveiligerType'
    definition = 'De verschillende types van obstakelbeveiliger.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACObstakelbeveiligerType'
    options = {
        'afstoppend-(NR)': KeuzelijstWaarde(invulwaarde='afstoppend-(NR)',
                                            label='afstoppend (NR)',
                                            status='ingebruik',
                                            definitie='Obstakelbeveiliger brengt het voertuig tot stilstand maar zijn niet getest op zijdelingse aanrijdingen',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACObstakelbeveiligerType/afstoppend-(NR)'),
        'geleidend-(R)': KeuzelijstWaarde(invulwaarde='geleidend-(R)',
                                          label='geleidend (R)',
                                          status='ingebruik',
                                          definitie='Obstakelbeveiliger brengt het voertuig niet tot stilstand maar terug in de juiste richting',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACObstakelbeveiligerType/geleidend-(R)')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

