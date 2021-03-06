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
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDekselKlasse'
    options = {
        'C250-(voetpad)': KeuzelijstWaarde(invulwaarde='C250-(voetpad)',
                                           label='C250 (voetpad)',
                                           status='ingebruik',
                                           definitie='C250 (voetpad)',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKlasse/C250-(voetpad)'),
        'D400-(rijweg)': KeuzelijstWaarde(invulwaarde='D400-(rijweg)',
                                          label='D400 (rijweg)',
                                          status='ingebruik',
                                          definitie='D400 (rijweg)',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKlasse/D400-(rijweg)'),
        'E600-(rijweg-voor-zwaar-verkeer)': KeuzelijstWaarde(invulwaarde='E600-(rijweg-voor-zwaar-verkeer)',
                                                             label='E600 (rijweg voor zwaar verkeer)',
                                                             status='ingebruik',
                                                             definitie='E600 (rijweg voor zwaar verkeer)',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKlasse/E600-(rijweg-voor-zwaar-verkeer)'),
        'F900-(vliegvelden)': KeuzelijstWaarde(invulwaarde='F900-(vliegvelden)',
                                               label='F900 (vliegvelden)',
                                               status='ingebruik',
                                               definitie='F900 (vliegvelden)',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselKlasse/F900-(vliegvelden)')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

