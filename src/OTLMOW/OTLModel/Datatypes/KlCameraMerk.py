# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCameraMerk(KeuzelijstField):
    """Het merk van de camera."""
    naam = 'KlCameraMerk'
    label = 'Camera merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCameraMerk'
    definition = 'Het merk van de camera.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCameraMerk'
    options = {
        'bosch': KeuzelijstWaarde(invulwaarde='bosch',
                                  label='Bosch',
                                  status='ingebruik',
                                  definitie='Bosch',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraMerk/bosch'),
        'videotec': KeuzelijstWaarde(invulwaarde='videotec',
                                     label='Videotec',
                                     status='ingebruik',
                                     definitie='Videotec',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraMerk/videotec')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

