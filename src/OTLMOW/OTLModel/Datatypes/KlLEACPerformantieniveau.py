# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACPerformantieniveau(KeuzelijstField):
    """De verschillende performantieniveaus van de afschermende constructies."""
    naam = 'KlLEACPerformantieniveau'
    label = 'Performantieniveau'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACPerformantieniveau'
    definition = 'De verschillende performantieniveaus van de afschermende constructies.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACPerformantieniveau'
    options = {
        '100': KeuzelijstWaarde(invulwaarde='100',
                                label='100',
                                status='ingebruik',
                                definitie='Obstakelbeveiliger getest aan 100km/h',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieniveau/100'),
        '110': KeuzelijstWaarde(invulwaarde='110',
                                label='110',
                                status='ingebruik',
                                definitie='Obstakelbeveiliger getest aan 110km/h',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieniveau/110'),
        '50': KeuzelijstWaarde(invulwaarde='50',
                               label='50',
                               status='ingebruik',
                               definitie='Obstakelbeveiliger beperkt getest aan 50km/h',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieniveau/50'),
        '80': KeuzelijstWaarde(invulwaarde='80',
                               label='80',
                               status='ingebruik',
                               definitie='Obstakelbeveiliger getest aan 80km/h',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieniveau/80'),
        '80-1': KeuzelijstWaarde(invulwaarde='80-1',
                                 label='80-1',
                                 status='ingebruik',
                                 definitie='Obstakelbeveiliger beperkt getest aan 80km/h ',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieniveau/80-1')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

