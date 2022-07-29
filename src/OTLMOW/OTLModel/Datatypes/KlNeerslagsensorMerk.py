# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNeerslagsensorMerk(KeuzelijstField):
    """Het merk van de neerslagsensor."""
    naam = 'KlNeerslagsensorMerk'
    label = 'Neerslagsensor merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNeerslagsensorMerk'
    definition = 'Het merk van de neerslagsensor.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNeerslagsensorMerk'
    options = {
        'Luft': KeuzelijstWaarde(invulwaarde='Luft',
                                 label='Luft',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNeerslagsensorMerk/Luft')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

