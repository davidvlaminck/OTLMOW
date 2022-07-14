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
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTelecommunicationsSubthema'
    options = {
        'elektronischecommunicatie': KeuzelijstWaarde(invulwaarde='elektronischecommunicatie',
                                                      label='elektronischeCommunicatie',
                                                      status='ingebruik',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecommunicationsSubthema/elektronischecommunicatie')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

