# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDekselKlasse(KeuzelijstField):
    """Klassen van het deksel van de bovenbouw."""
    naam = 'KlDekselKlasse'
    label = 'Dekselklasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDekselKlasse'
    definition = 'Klassen van het deksel van de bovenbouw.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDekselKlasse'
    options = {
        'C250-(voetpad)': KeuzelijstWaarde(invulwaarde='C250-(voetpad)',
                                           label='C250 (voetpad)',
                                           status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='C250 (voetpad)',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKlasse/C250-(voetpad)'),
        'D400-(rijweg)': KeuzelijstWaarde(invulwaarde='D400-(rijweg)',
                                          label='D400 (rijweg)',
                                          status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='D400 (rijweg)',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKlasse/D400-(rijweg)'),
        'E600-(rijweg-voor-zwaar-verkeer)': KeuzelijstWaarde(invulwaarde='E600-(rijweg-voor-zwaar-verkeer)',
                                                             label='E600 (rijweg voor zwaar verkeer)',
                                                             status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                             definitie='E600 (rijweg voor zwaar verkeer)',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKlasse/E600-(rijweg-voor-zwaar-verkeer)'),
        'F900-(vliegvelden)': KeuzelijstWaarde(invulwaarde='F900-(vliegvelden)',
                                               label='F900 (vliegvelden)',
                                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                               definitie='F900 (vliegvelden)',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKlasse/F900-(vliegvelden)')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlDekselKlasse.get_dummy_data()

