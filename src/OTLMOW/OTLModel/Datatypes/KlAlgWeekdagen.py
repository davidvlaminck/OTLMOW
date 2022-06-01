# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgWeekdagen(KeuzelijstField):
    """Lijst van de verschillende weekdagen."""
    naam = 'KlAlgWeekdagen'
    label = 'Weekdagen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgWeekdagen'
    definition = 'Lijst van de verschillende weekdagen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgWeekdagen'
    options = {
        'dinsdag': KeuzelijstWaarde(invulwaarde='dinsdag',
                                    label='dinsdag',
                                    definitie='De dag van een week tussen maandag en woensdag.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/dinsdag'),
        'donderdag': KeuzelijstWaarde(invulwaarde='donderdag',
                                      label='donderdag',
                                      definitie='De dag van een week tussen woensdag en vrijdag.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/donderdag'),
        'feestdag': KeuzelijstWaarde(invulwaarde='feestdag',
                                     label='feestdag',
                                     definitie='Een wettelijke nationale vrije dag.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/feestdag'),
        'maandag': KeuzelijstWaarde(invulwaarde='maandag',
                                    label='maandag',
                                    definitie='De dag van een week tussen zondag en dinsdag.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/maandag'),
        'vrijdag': KeuzelijstWaarde(invulwaarde='vrijdag',
                                    label='vrijdag',
                                    definitie='De dag van een week tussen donderdag en zaterdag.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/vrijdag'),
        'woensdag': KeuzelijstWaarde(invulwaarde='woensdag',
                                     label='woensdag',
                                     definitie='De dag van een week tussen dinsdag en donderdag.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/woensdag'),
        'zaterdag': KeuzelijstWaarde(invulwaarde='zaterdag',
                                     label='zaterdag',
                                     definitie='De dag van een week tussen vrijdag en zondag.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/zaterdag'),
        'zondag': KeuzelijstWaarde(invulwaarde='zondag',
                                   label='zondag',
                                   definitie='De dag van een week tussen zaterdag en maandag.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/zondag')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlAlgWeekdagen.get_dummy_data()

