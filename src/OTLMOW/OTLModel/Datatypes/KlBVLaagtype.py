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
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBVLaagtype'
    options = {
        'andere-toplagen': KeuzelijstWaarde(invulwaarde='andere-toplagen',
                                            label='andere toplagen',
                                            definitie='union type om het laagtype van bitumineuze verharding te bepalen',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVLaagtype/andere-toplagen'),
        'beschermingslaag': KeuzelijstWaarde(invulwaarde='beschermingslaag',
                                             label='beschermingslaag',
                                             definitie='beschermingslaag',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVLaagtype/beschermingslaag'),
        'onderlaag': KeuzelijstWaarde(invulwaarde='onderlaag',
                                      label='onderlaag',
                                      definitie='Onderliggende laag van een bitumineuze verharding met een constante dikte. ',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVLaagtype/onderlaag'),
        'profileerlaag': KeuzelijstWaarde(invulwaarde='profileerlaag',
                                          label='profileerlaag',
                                          definitie='union type om het laagtype van bitumineuze verharding te bepalen',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVLaagtype/profileerlaag'),
        'toplaag-van-asfaltbeton': KeuzelijstWaarde(invulwaarde='toplaag-van-asfaltbeton',
                                                    label='toplaag van asfaltbeton',
                                                    definitie='Bovenste laag van een bitumineuze verharding, die direct in contact komt met het verkeer bestaande uit asfaltbeton.',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVLaagtype/toplaag-van-asfaltbeton'),
        'toplaag-van-gietasfalt': KeuzelijstWaarde(invulwaarde='toplaag-van-gietasfalt',
                                                   label='toplaag van gietasfalt',
                                                   definitie='union type om het laagtype van bitumineuze verharding te bepalen',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVLaagtype/toplaag-van-gietasfalt'),
        'tussenlaag': KeuzelijstWaarde(invulwaarde='tussenlaag',
                                       label='tussenlaag',
                                       definitie='Bitumineuze laag die aangebracht wordt tussen een betonverharding en de fundering. ',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVLaagtype/tussenlaag')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBVLaagtype.get_dummy_data()

