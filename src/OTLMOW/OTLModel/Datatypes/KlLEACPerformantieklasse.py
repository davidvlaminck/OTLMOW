# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACPerformantieklasse(KeuzelijstField):
    """De verschillende performantieklasses van de geteste beginconstructie."""
    naam = 'KlLEACPerformantieklasse'
    label = 'Performantieklasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACPerformantieklasse'
    definition = 'De verschillende performantieklasses van de geteste beginconstructie.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACPerformantieklasse'
    options = {
        'P1': KeuzelijstWaarde(invulwaarde='P1',
                               label='P1',
                               definitie='Beginconstructie enkel frontaal getest met een lichte wagen aan 80km/h',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieklasse/P1'),
        'P2': KeuzelijstWaarde(invulwaarde='P2',
                               label='P2',
                               definitie='Beginconstructie zowel frontaal als zijwaarts getest, met een lichte en kleine gezinswagen aan 80km/h',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieklasse/P2'),
        'P3': KeuzelijstWaarde(invulwaarde='P3',
                               label='P3',
                               definitie='Beginconstructie zowel frontaal als zijwaarts getest, met een lichte en kleine gezinswagen aan 100km/h',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieklasse/P3'),
        'P4': KeuzelijstWaarde(invulwaarde='P4',
                               label='P4',
                               definitie='Beginconstructie zowel frontaal als zijwaarts getest, met een lichte en grote gezinswagen aan 110km/h',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieklasse/P4')
    }

