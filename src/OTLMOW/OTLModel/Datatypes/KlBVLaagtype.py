# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBVLaagtype(KeuzelijstField):
    """Laagtypes van de bitumineuze verharding."""
    naam = 'KlBVLaagtype'
    label = 'BV laagtype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBVLaagtype'
    definition = 'Laagtypes van de bitumineuze verharding.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBVLaagtype'
    options = {
        'andere-toplagen': KeuzelijstWaarde(invulwaarde='andere-toplagen',
                                            label='andere toplagen',
                                            status='ingebruik',
                                            definitie='union type om het laagtype van bitumineuze verharding te bepalen',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVLaagtype/andere-toplagen'),
        'beschermingslaag': KeuzelijstWaarde(invulwaarde='beschermingslaag',
                                             label='beschermingslaag',
                                             status='ingebruik',
                                             definitie='beschermingslaag',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVLaagtype/beschermingslaag'),
        'onderlaag': KeuzelijstWaarde(invulwaarde='onderlaag',
                                      label='onderlaag',
                                      status='ingebruik',
                                      definitie='Onderliggende laag van een bitumineuze verharding met een constante dikte. ',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVLaagtype/onderlaag'),
        'profileerlaag': KeuzelijstWaarde(invulwaarde='profileerlaag',
                                          label='profileerlaag',
                                          status='ingebruik',
                                          definitie='union type om het laagtype van bitumineuze verharding te bepalen',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVLaagtype/profileerlaag'),
        'toplaag-van-asfaltbeton': KeuzelijstWaarde(invulwaarde='toplaag-van-asfaltbeton',
                                                    label='toplaag van asfaltbeton',
                                                    status='ingebruik',
                                                    definitie='Bovenste laag van een bitumineuze verharding, die direct in contact komt met het verkeer bestaande uit asfaltbeton.',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVLaagtype/toplaag-van-asfaltbeton'),
        'toplaag-van-gietasfalt': KeuzelijstWaarde(invulwaarde='toplaag-van-gietasfalt',
                                                   label='toplaag van gietasfalt',
                                                   status='ingebruik',
                                                   definitie='union type om het laagtype van bitumineuze verharding te bepalen',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVLaagtype/toplaag-van-gietasfalt'),
        'tussenlaag': KeuzelijstWaarde(invulwaarde='tussenlaag',
                                       label='tussenlaag',
                                       status='ingebruik',
                                       definitie='Bitumineuze laag die aangebracht wordt tussen een betonverharding en de fundering. ',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVLaagtype/tussenlaag')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

