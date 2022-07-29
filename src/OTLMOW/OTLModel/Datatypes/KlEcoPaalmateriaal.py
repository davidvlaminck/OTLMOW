# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEcoPaalmateriaal(KeuzelijstField):
    """Materialen van de paal in het ecoraster."""
    naam = 'KlEcoPaalmateriaal'
    label = 'Paalmateriaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEcoPaalmateriaal'
    definition = 'Materialen van de paal in het ecoraster.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEcoPaalmateriaal'
    options = {
        'hout-Kastanje': KeuzelijstWaarde(invulwaarde='hout-Kastanje',
                                          label='hout Kastanje',
                                          status='ingebruik',
                                          definitie='Een houten paal van kastanje hout.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoPaalmateriaal/hout-Kastanje'),
        'hout-Robina': KeuzelijstWaarde(invulwaarde='hout-Robina',
                                        label='hout Robina',
                                        status='ingebruik',
                                        definitie='Een houten paal van robina hout.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoPaalmateriaal/hout-Robina'),
        'metaal': KeuzelijstWaarde(invulwaarde='metaal',
                                   label='metaal',
                                   status='ingebruik',
                                   definitie='Een metalen paal.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoPaalmateriaal/metaal')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

