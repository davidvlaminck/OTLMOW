# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVriLusSoortvoertuig(KeuzelijstField):
    """Keuzelijst met verschillende types voertuigen die een detectielus volgens diens instellingen kan detecteren."""
    naam = 'KlVriLusSoortvoertuig'
    label = 'VRI-lus soort voertuig'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVriLusSoortvoertuig'
    definition = 'Keuzelijst met verschillende types voertuigen die een detectielus volgens diens instellingen kan detecteren.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVriLusSoortvoertuig'
    options = {
        'fiets': KeuzelijstWaarde(invulwaarde='fiets',
                                  label='fiets',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusSoortvoertuig/fiets'),
        'motor': KeuzelijstWaarde(invulwaarde='motor',
                                  label='motor',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusSoortvoertuig/motor'),
        'voertuig': KeuzelijstWaarde(invulwaarde='voertuig',
                                     label='voertuig',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusSoortvoertuig/voertuig')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlVriLusSoortvoertuig.get_dummy_data()

