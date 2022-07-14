# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeschermingMaaischade(KeuzelijstField):
    """De middelen als bescherming tegen maaischade."""
    naam = 'KlBeschermingMaaischade'
    label = 'Bescherming maaischade'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBeschermingMaaischade'
    definition = 'De middelen als bescherming tegen maaischade.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeschermingMaaischade'
    options = {
        'houten-paal': KeuzelijstWaarde(invulwaarde='houten-paal',
                                        label='houten paal',
                                        status='ingebruik',
                                        definitie='Bescherming dmv een houten paal.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermingMaaischade/houten-paal'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='kunststof',
                                      status='ingebruik',
                                      definitie='Bescherming in kunststof.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermingMaaischade/kunststof')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

