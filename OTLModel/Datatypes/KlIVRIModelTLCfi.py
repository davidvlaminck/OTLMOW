# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIModelTLCfi(KeuzelijstField):
    """De modelnaam van de TLC-fi poort."""
    naam = 'KlIVRIModelTLCfi'
    label = 'iVRIModelTLCfi'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIVRIModelTLCfi'
    definition = 'De modelnaam van de TLC-fi poort.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIModelTLCfi'
    options = {
        'civa-2020': KeuzelijstWaarde(invulwaarde='civa-2020',
                                      label='CIVA 2020',
                                      definitie='CIVA 2020',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIModelTLCfi/civa-2020'),
        'flownode': KeuzelijstWaarde(invulwaarde='flownode',
                                     label='FlowNode',
                                     definitie='FlowNode',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIModelTLCfi/flownode'),
        'tlc-fi-broker': KeuzelijstWaarde(invulwaarde='tlc-fi-broker',
                                          label='TLC-FI broker',
                                          definitie='TLC-FI broker',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIModelTLCfi/tlc-fi-broker')
    }

