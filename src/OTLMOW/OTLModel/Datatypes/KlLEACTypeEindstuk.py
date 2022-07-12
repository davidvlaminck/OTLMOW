# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACTypeEindstuk(KeuzelijstField):
    """De verschillende types eindstukken."""
    naam = 'KlLEACTypeEindstuk'
    label = 'Type eindstuk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACTypeEindstuk'
    definition = 'De verschillende types eindstukken.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACTypeEindstuk'
    options = {
        'naar-beneden-afgebogen': KeuzelijstWaarde(invulwaarde='naar-beneden-afgebogen',
                                                   label='naar beneden afgebogen',
                                                   status='ingebruik',
                                                   definitie='naar beneden afgebogen',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACTypeEindstuk/naar-beneden-afgebogen'),
        'schelp': KeuzelijstWaarde(invulwaarde='schelp',
                                   label='schelp',
                                   status='ingebruik',
                                   definitie='schelp',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACTypeEindstuk/schelp'),
        'uitgebogen': KeuzelijstWaarde(invulwaarde='uitgebogen',
                                       label='uitgebogen',
                                       status='ingebruik',
                                       definitie='uitgebogen',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACTypeEindstuk/uitgebogen')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlLEACTypeEindstuk.get_dummy_data()

