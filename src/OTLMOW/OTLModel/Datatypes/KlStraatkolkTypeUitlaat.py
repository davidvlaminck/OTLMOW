# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStraatkolkTypeUitlaat(KeuzelijstField):
    """Het type van uitlaat van de straatkolk."""
    naam = 'KlStraatkolkTypeUitlaat'
    label = 'straatkolk type uitlaat '
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStraatkolkTypeUitlaat'
    definition = 'Het type van uitlaat van de straatkolk.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStraatkolkTypeUitlaat'
    options = {
        'kop-uitlaat': KeuzelijstWaarde(invulwaarde='kop-uitlaat',
                                        label='kop uitlaat',
                                        status='ingebruik',
                                        definitie='kop uitlaat',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkTypeUitlaat/kop-uitlaat'),
        'onderuitlaat': KeuzelijstWaarde(invulwaarde='onderuitlaat',
                                         label='onderuitlaat',
                                         status='ingebruik',
                                         definitie='onderuitlaat',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkTypeUitlaat/onderuitlaat'),
        'zij-uitlaat': KeuzelijstWaarde(invulwaarde='zij-uitlaat',
                                        label='zij uitlaat',
                                        status='ingebruik',
                                        definitie='zij uitlaat',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkTypeUitlaat/zij-uitlaat')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

