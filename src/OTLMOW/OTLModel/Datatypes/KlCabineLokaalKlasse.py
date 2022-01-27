# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCabineLokaalKlasse(KeuzelijstField):
    """Lijst van waarden voor de classificatie van de hoogspanningscabine als lokaal volgens Synergrid."""
    naam = 'KlCabineLokaalKlasse'
    label = 'Cabine lokaal klasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCabineLokaalKlasse'
    definition = 'Lijst van waarden voor de classificatie van de hoogspanningscabine als lokaal volgens Synergrid.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCabineLokaalKlasse'
    options = {
        'BB00': KeuzelijstWaarde(invulwaarde='BB00',
                                 label='BB00',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineLokaalKlasse/BB00'),
        'BB05': KeuzelijstWaarde(invulwaarde='BB05',
                                 label='BB05',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineLokaalKlasse/BB05'),
        'BB10': KeuzelijstWaarde(invulwaarde='BB10',
                                 label='BB10',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineLokaalKlasse/BB10'),
        'BB20': KeuzelijstWaarde(invulwaarde='BB20',
                                 label='BB20',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineLokaalKlasse/BB20'),
        'BB30': KeuzelijstWaarde(invulwaarde='BB30',
                                 label='BB30',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineLokaalKlasse/BB30'),
        'BB40': KeuzelijstWaarde(invulwaarde='BB40',
                                 label='BB40',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineLokaalKlasse/BB40'),
        'BB50': KeuzelijstWaarde(invulwaarde='BB50',
                                 label='BB50',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineLokaalKlasse/BB50')
    }

