# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGPUMerk(KeuzelijstField):
    """Het merk van de GPU."""
    naam = 'KlGPUMerk'
    label = 'GPU merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGPUMerk'
    definition = 'Het merk van de GPU.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGPUMerk'
    options = {
        'nvidia': KeuzelijstWaarde(invulwaarde='nvidia',
                                   label='Nvidia',
                                   definitie='Nvidia',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGPUMerk/nvidia')
    }

