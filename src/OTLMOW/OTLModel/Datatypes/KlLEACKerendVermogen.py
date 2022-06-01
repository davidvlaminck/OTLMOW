# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACKerendVermogen(KeuzelijstField):
    """De verschillende niveaus van kerend vermogen gedefinieerd : van T1 (laagste niveau) tot H4b (hoogste niveau)  Voor elk kerend vermogen wordt in de norm precies vastgelegd welke botsproeven moeten uitgevoerd worden."""
    naam = 'KlLEACKerendVermogen'
    label = 'Kerend vermogen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACKerendVermogen'
    definition = 'De verschillende niveaus van kerend vermogen gedefinieerd : van T1 (laagste niveau) tot H4b (hoogste niveau)  Voor elk kerend vermogen wordt in de norm precies vastgelegd welke botsproeven moeten uitgevoerd worden.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACKerendVermogen'
    options = {
        'H1': KeuzelijstWaarde(invulwaarde='H1',
                               label='H1',
                               definitie='hoog kerend vermogen, getest met een vrachtwagen van 10 ton',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACKerendVermogen/H1'),
        'H2': KeuzelijstWaarde(invulwaarde='H2',
                               label='H2',
                               definitie='hoog kerend vermogen, getest met een bus van 13 ton',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACKerendVermogen/H2'),
        'H3': KeuzelijstWaarde(invulwaarde='H3',
                               label='H3',
                               definitie='hoog kerend vermogen, getest met een vrachtwagen van 16 ton',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACKerendVermogen/H3'),
        'H4a': KeuzelijstWaarde(invulwaarde='H4a',
                                label='H4a',
                                definitie='zeer hoog kerend vermogen, getest met een vrachtwagen van 30 ton',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACKerendVermogen/H4a'),
        'H4b': KeuzelijstWaarde(invulwaarde='H4b',
                                label='H4b',
                                definitie='zeer hoog kerend vermogen, getest met een vrachtwagen van 38 ton',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACKerendVermogen/H4b'),
        'N1': KeuzelijstWaarde(invulwaarde='N1',
                               label='N1',
                               definitie='normaal kerend vermogen, getest met een wagen',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACKerendVermogen/N1'),
        'N2': KeuzelijstWaarde(invulwaarde='N2',
                               label='N2',
                               definitie='normaal kerend vermogen, getest met een wagen aan hoge snelheid',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACKerendVermogen/N2'),
        'T1': KeuzelijstWaarde(invulwaarde='T1',
                               label='T1',
                               definitie='kerend vermogen voor lage impacthoeken, geschikt voor tijdelijke situaties, getest met een wagen',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACKerendVermogen/T1'),
        'T2': KeuzelijstWaarde(invulwaarde='T2',
                               label='T2',
                               definitie='kerend vermogen voor lage impacthoeken, geschikt voor tijdelijke situaties, getest met een wagen maar voor hogere impacthoeken dan T1',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACKerendVermogen/T2'),
        'T3': KeuzelijstWaarde(invulwaarde='T3',
                               label='T3',
                               definitie='kerend vermogen voor lage impacthoeken, geschikt voor tijdelijke situaties, getest met een vrachtwagen',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACKerendVermogen/T3')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlLEACKerendVermogen.get_dummy_data()

