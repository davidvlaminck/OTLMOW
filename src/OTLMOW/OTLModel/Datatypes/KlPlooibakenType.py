# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPlooibakenType(KeuzelijstField):
    """ vormen van een plooibaken."""
    naam = 'KlPlooibakenType'
    label = 'Plooibaken type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPlooibakenType'
    definition = ' vormen van een plooibaken.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPlooibakenType'
    options = {
        'plooibaken-diameter-130-mm---M24': KeuzelijstWaarde(invulwaarde='plooibaken-diameter-130-mm---M24',
                                                             label='plooibaken diameter 130 mm - M24',
                                                             definitie='Plooibaken diameter 130 mm – M24',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlooibakenType/plooibaken-diameter-130-mm---M24'),
        'plooibaken-diameter-80-mm---M16': KeuzelijstWaarde(invulwaarde='plooibaken-diameter-80-mm---M16',
                                                            label='plooibaken diameter 80 mm - M16',
                                                            definitie='Plooibaken diameter 80 mm – M16',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlooibakenType/plooibaken-diameter-80-mm---M16'),
        'plooibaken-diameter-80-mm---M24': KeuzelijstWaarde(invulwaarde='plooibaken-diameter-80-mm---M24',
                                                            label='plooibaken diameter 80 mm - M24',
                                                            definitie='Plooibaken diameter 80 mm – M24',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlooibakenType/plooibaken-diameter-80-mm---M24'),
        'verkeerszuil': KeuzelijstWaarde(invulwaarde='verkeerszuil',
                                         label='verkeerszuil',
                                         definitie='Verkeerszuil',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlooibakenType/verkeerszuil')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlPlooibakenType.get_dummy_data()

