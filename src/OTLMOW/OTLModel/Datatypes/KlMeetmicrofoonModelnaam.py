# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMeetmicrofoonModelnaam(KeuzelijstField):
    """De modelnaam van de meetmicrofoon."""
    naam = 'KlMeetmicrofoonModelnaam'
    label = 'Meetmicrofoon modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMeetmicrofoonModelnaam'
    definition = 'De modelnaam van de meetmicrofoon.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMeetmicrofoonModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

