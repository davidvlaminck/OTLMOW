# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMarkeringWaarborgperiode(KeuzelijstField):
    """Opties om de waarborgperiode aan te duiden."""
    naam = 'KlMarkeringWaarborgperiode'
    label = 'markeringswaarborgperiode'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMarkeringWaarborgperiode'
    definition = 'Opties om de waarborgperiode aan te duiden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMarkeringWaarborgperiode'
    options = {
        '1-jaar': KeuzelijstWaarde(invulwaarde='1-jaar',
                                   label='1 jaar',
                                   status='ingebruik',
                                   definitie='Waarborgperiode van 1 jaar.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringWaarborgperiode/1-jaar'),
        '3-jaar': KeuzelijstWaarde(invulwaarde='3-jaar',
                                   label='3 jaar',
                                   status='ingebruik',
                                   definitie='Waarborgperiode van 3 jaar.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringWaarborgperiode/3-jaar'),
        '6-jaar': KeuzelijstWaarde(invulwaarde='6-jaar',
                                   label='6 jaar',
                                   status='ingebruik',
                                   definitie='Waarborgperiode van 6 jaar.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringWaarborgperiode/6-jaar')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

