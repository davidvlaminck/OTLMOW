# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIMerkRIS(KeuzelijstField):
    """Het merk van de RIS."""
    naam = 'KlIVRIMerkRIS'
    label = 'iVRIMerkRIS'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIVRIMerkRIS'
    definition = 'Het merk van de RIS.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIMerkRIS'
    options = {
        'peek': KeuzelijstWaarde(invulwaarde='peek',
                                 label='Peek',
                                 status='ingebruik',
                                 definitie='Peek',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIMerkRIS/peek'),
        'swarco': KeuzelijstWaarde(invulwaarde='swarco',
                                   label='Swarco',
                                   status='ingebruik',
                                   definitie='Swarco',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIMerkRIS/swarco')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

