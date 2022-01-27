# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlANPRMerk(KeuzelijstField):
    """Het merk van de ANPR-camera."""
    naam = 'KlANPRMerk'
    label = 'ANPR-camera merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlANPRMerk'
    definition = 'Het merk van de ANPR-camera.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlANPRMerk'
    options = {
        'Macq': KeuzelijstWaarde(invulwaarde='Macq',
                                 label='Macq',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRMerk/Macq'),
        'Tattile': KeuzelijstWaarde(invulwaarde='Tattile',
                                    label='Tattile',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRMerk/Tattile')
    }

