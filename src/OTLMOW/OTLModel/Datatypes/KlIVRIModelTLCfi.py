# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIModelTLCfi(KeuzelijstField):
    """De modelnaam van de TLC-fi poort."""
    naam = 'KlIVRIModelTLCfi'
    label = 'iVRIModelTLCfi'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIVRIModelTLCfi'
    definition = 'De modelnaam van de TLC-fi poort.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIModelTLCfi'
    options = {
        'civa-2020': KeuzelijstWaarde(invulwaarde='civa-2020',
                                      label='CIVA 2020',
                                      status='ingebruik',
                                      definitie='CIVA 2020',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIModelTLCfi/civa-2020'),
        'flownode': KeuzelijstWaarde(invulwaarde='flownode',
                                     label='FlowNode',
                                     status='ingebruik',
                                     definitie='FlowNode',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIModelTLCfi/flownode'),
        'tlc-fi-broker': KeuzelijstWaarde(invulwaarde='tlc-fi-broker',
                                          label='TLC-FI broker',
                                          status='ingebruik',
                                          definitie='TLC-FI broker',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIModelTLCfi/tlc-fi-broker')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlIVRIModelTLCfi.get_dummy_data()

