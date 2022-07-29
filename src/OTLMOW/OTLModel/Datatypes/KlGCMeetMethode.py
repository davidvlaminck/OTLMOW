# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGCMeetMethode(KeuzelijstField):
    """Locaties van de geluidstestproef."""
    naam = 'KlGCMeetMethode'
    label = 'Meet methode'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGCMeetMethode'
    definition = 'Locaties van de geluidstestproef.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGCMeetMethode'
    options = {
        'inSitu': KeuzelijstWaarde(invulwaarde='inSitu',
                                   label='inSitu',
                                   status='ingebruik',
                                   definitie='Proef uitgevoerd op de werf',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGCMeetMethode/inSitu'),
        'labo': KeuzelijstWaarde(invulwaarde='labo',
                                 label='labo',
                                 status='ingebruik',
                                 definitie='Proef uitgevoerd in het labo',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGCMeetMethode/labo')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

