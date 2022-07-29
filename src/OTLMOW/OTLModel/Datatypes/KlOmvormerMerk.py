# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOmvormerMerk(KeuzelijstField):
    """Het merk van de omvormer."""
    naam = 'KlOmvormerMerk'
    label = 'Omvormer merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOmvormerMerk'
    definition = 'Het merk van de omvormer.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOmvormerMerk'
    options = {
        'axis': KeuzelijstWaarde(invulwaarde='axis',
                                 label='Axis',
                                 status='ingebruik',
                                 definitie='Axis',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerMerk/axis'),
        'bosch': KeuzelijstWaarde(invulwaarde='bosch',
                                  label='Bosch',
                                  status='ingebruik',
                                  definitie='Bosch',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerMerk/bosch')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

