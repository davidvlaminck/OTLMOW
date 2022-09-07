# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIMerkITSapp(KeuzelijstField):
    """Het merk van de ITSapp."""
    naam = 'KlIVRIMerkITSapp'
    label = 'iVRIMerkITSapp'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIVRIMerkITSapp'
    definition = 'Het merk van de ITSapp.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIMerkITSapp'
    options = {
        'peek': KeuzelijstWaarde(invulwaarde='peek',
                                 label='Peek',
                                 status='ingebruik',
                                 definitie='Peek',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIMerkITSapp/peek'),
        'rhdhv': KeuzelijstWaarde(invulwaarde='rhdhv',
                                  label='RHDHV',
                                  status='ingebruik',
                                  definitie='RHDHV',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIMerkITSapp/rhdhv')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

