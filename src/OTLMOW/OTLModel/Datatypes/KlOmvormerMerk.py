# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOmvormerMerk(KeuzelijstField):
    """Het merk van de omvormer."""
    naam = 'KlOmvormerMerk'
    label = 'Omvormer merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOmvormerMerk'
    definition = 'Het merk van de omvormer.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOmvormerMerk'
    options = {
        'axis': KeuzelijstWaarde(invulwaarde='axis',
                                 label='Axis',
                                 definitie='Axis',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerMerk/axis'),
        'bosch': KeuzelijstWaarde(invulwaarde='bosch',
                                  label='Bosch',
                                  definitie='Bosch',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerMerk/bosch')
    }

