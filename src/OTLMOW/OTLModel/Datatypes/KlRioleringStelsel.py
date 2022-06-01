# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRioleringStelsel(KeuzelijstField):
    """Stelsels van de riool."""
    naam = 'KlRioleringStelsel'
    label = 'Riolering stelsel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRioleringStelsel'
    definition = 'Stelsels van de riool.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRioleringStelsel'
    options = {
        'drain': KeuzelijstWaarde(invulwaarde='drain',
                                  label='drain',
                                  definitie='Stelsel om grondwater op te vangen en af te voeren.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringStelsel/drain'),
        'infiltratie': KeuzelijstWaarde(invulwaarde='infiltratie',
                                        label='infiltratie',
                                        definitie='Het water in het systeem kan rechtstreeks in de grond infiltreren.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringStelsel/infiltratie'),
        'n-vuil': KeuzelijstWaarde(invulwaarde='n-vuil',
                                   label='n vuil',
                                   definitie='Stelsel bedoeld voor de afvoer van onvervuild water. Het deksel van dit stelsel kan de code RWA (regenwaterafvoer) of W (eigendom van de watermaatschappij) hebben.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringStelsel/n-vuil'),
        'onbekend': KeuzelijstWaarde(invulwaarde='onbekend',
                                     label='onbekend',
                                     definitie='Stelsel waarvan afvoer onbekend is.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringStelsel/onbekend'),
        'vuil': KeuzelijstWaarde(invulwaarde='vuil',
                                 label='vuil',
                                 definitie='Stelsel bedoeld voor de afvoer van vervuild water. Het deksel van dit stelsel kan de code DWA (sterk geconcentreerd afvalwater), DRWA (combinatie van regenwater en afvalwater) of W (eigendom van de watermaatschappij) hebben.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringStelsel/vuil')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlRioleringStelsel.get_dummy_data()

