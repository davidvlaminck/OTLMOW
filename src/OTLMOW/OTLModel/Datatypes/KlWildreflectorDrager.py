# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWildreflectorDrager(KeuzelijstField):
    """Mogelijke dragers van een wildreflector."""
    naam = 'KlWildreflectorDrager'
    label = 'Wildreflector drager'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWildreflectorDrager'
    definition = 'Mogelijke dragers van een wildreflector.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWildreflectorDrager'
    options = {
        'houten-paal': KeuzelijstWaarde(invulwaarde='houten-paal',
                                        label='houten paal',
                                        status='ingebruik',
                                        definitie='houten paal als drager.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWildreflectorDrager/houten-paal'),
        'metalen-paal': KeuzelijstWaarde(invulwaarde='metalen-paal',
                                         label='metalen paal',
                                         status='ingebruik',
                                         definitie='metalen paal als drager.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWildreflectorDrager/metalen-paal')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

