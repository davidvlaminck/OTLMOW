# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIModelRIS(KeuzelijstField):
    """De modelnaam van de RIS."""
    naam = 'KlIVRIModelRIS'
    label = 'iVRIModelRIS'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIVRIModelRIS'
    definition = 'De modelnaam van de RIS.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIModelRIS'
    options = {
        'virtualacu': KeuzelijstWaarde(invulwaarde='virtualacu',
                                       label='VirtualACU',
                                       status='ingebruik',
                                       definitie='VirtualACU',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIModelRIS/virtualacu')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

