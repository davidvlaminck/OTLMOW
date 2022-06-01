# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomGroeifase(KeuzelijstField):
    """De verschillende fases van beheer volgens de verschillende levensfases."""
    naam = 'KlBoomGroeifase'
    label = 'Groeifasen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomGroeifase'
    definition = 'De verschillende fases van beheer volgens de verschillende levensfases.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomGroeifase'
    options = {
        'dood': KeuzelijstWaarde(invulwaarde='dood',
                                 label='dood',
                                 definitie='Dood',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGroeifase/dood'),
        'eindfase': KeuzelijstWaarde(invulwaarde='eindfase',
                                     label='eindfase',
                                     definitie='De periode waarbij regressie/aftakeling plaatsvindt – beheer gericht op in stand houding (kroonverzorging)',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGroeifase/eindfase'),
        'jeugdfase': KeuzelijstWaarde(invulwaarde='jeugdfase',
                                      label='jeugdfase',
                                      definitie='De periode van de lengte-ontwikkeling van de boom – beheer gericht op tot stand brengen van de takvrije stamlengte (begeleidingssnoei,..)',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGroeifase/jeugdfase'),
        'plantfase': KeuzelijstWaarde(invulwaarde='plantfase',
                                      label='plantfase',
                                      definitie='De periode na de aanplant waarbij het beheer gericht is op het aanslaan van de boom (water geven, boompalen verwijderen,…)',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGroeifase/plantfase'),
        'volwassenfase': KeuzelijstWaarde(invulwaarde='volwassenfase',
                                          label='volwassenfase',
                                          definitie='De periode van de kroonontwikkeling – beheer gericht op in stand houden van de boom (onderhoudssnoei)',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGroeifase/volwassenfase')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBoomGroeifase.get_dummy_data()

