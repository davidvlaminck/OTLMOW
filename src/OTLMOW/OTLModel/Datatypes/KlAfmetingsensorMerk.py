# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfmetingsensorMerk(KeuzelijstField):
    """Het merk van de afmetingsensor."""
    naam = 'KlAfmetingsensorMerk'
    label = 'Afmetingsensor merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfmetingsensorMerk'
    definition = 'Het merk van de afmetingsensor.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfmetingsensorMerk'
    options = {
        'Sick': KeuzelijstWaarde(invulwaarde='Sick',
                                 label='Sick',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfmetingsensorMerk/Sick')
    }

