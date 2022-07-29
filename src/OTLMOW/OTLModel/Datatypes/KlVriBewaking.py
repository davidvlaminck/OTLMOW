# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVriBewaking(KeuzelijstField):
    """Keuzelijst met verschillende soorten bewaking of detectie bij een VRI."""
    naam = 'KlVriBewaking'
    label = 'VRI bewaking'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVriBewaking'
    definition = 'Keuzelijst met verschillende soorten bewaking of detectie bij een VRI.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVriBewaking'
    options = {
        'bewaakt-primair-alarm': KeuzelijstWaarde(invulwaarde='bewaakt-primair-alarm',
                                                  label='bewaakt primair alarm',
                                                  status='ingebruik',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriBewaking/bewaakt-primair-alarm'),
        'bewaakt-secundair-alarm': KeuzelijstWaarde(invulwaarde='bewaakt-secundair-alarm',
                                                    label='bewaakt secundair alarm',
                                                    status='ingebruik',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriBewaking/bewaakt-secundair-alarm'),
        'bewaakt-zonder-alarm': KeuzelijstWaarde(invulwaarde='bewaakt-zonder-alarm',
                                                 label='bewaakt zonder alarm',
                                                 status='ingebruik',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriBewaking/bewaakt-zonder-alarm'),
        'niet-bewaakt': KeuzelijstWaarde(invulwaarde='niet-bewaakt',
                                         label='niet bewaakt',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriBewaking/niet-bewaakt')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

