# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTelecommunicationsSubthema(KeuzelijstField):
    """Lijst voor classificatie van een kabels en appurtenance voor telecommunicatie."""
    naam = 'KlTelecommunicationsSubthema'
    label = 'Telecommunications subthema'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlTelecommunicationsSubthema'
    definition = 'Lijst voor classificatie van een kabels en appurtenance voor telecommunicatie.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTelecommunicationsSubthema'
    options = {
        'elektronischecommunicatie': KeuzelijstWaarde(invulwaarde='elektronischecommunicatie',
                                                      label='elektronischeCommunicatie',
                                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecommunicationsSubthema/elektronischecommunicatie')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlTelecommunicationsSubthema.get_dummy_data()

