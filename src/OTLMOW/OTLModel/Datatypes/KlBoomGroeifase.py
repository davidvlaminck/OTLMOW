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
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomGroeifase'
    options = {
        'dood': KeuzelijstWaarde(invulwaarde='dood',
                                 label='dood',
                                 status='ingebruik',
                                 definitie='Dood',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGroeifase/dood'),
        'eindfase': KeuzelijstWaarde(invulwaarde='eindfase',
                                     label='eindfase',
                                     status='ingebruik',
                                     definitie='De periode waarbij regressie/aftakeling plaatsvindt – beheer gericht op in stand houding (kroonverzorging)',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGroeifase/eindfase'),
        'jeugdfase': KeuzelijstWaarde(invulwaarde='jeugdfase',
                                      label='jeugdfase',
                                      status='ingebruik',
                                      definitie='De periode van de lengte-ontwikkeling van de boom – beheer gericht op tot stand brengen van de takvrije stamlengte (begeleidingssnoei,..)',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGroeifase/jeugdfase'),
        'plantfase': KeuzelijstWaarde(invulwaarde='plantfase',
                                      label='plantfase',
                                      status='ingebruik',
                                      definitie='De periode na de aanplant waarbij het beheer gericht is op het aanslaan van de boom (water geven, boompalen verwijderen,…)',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGroeifase/plantfase'),
        'volwassenfase': KeuzelijstWaarde(invulwaarde='volwassenfase',
                                          label='volwassenfase',
                                          status='ingebruik',
                                          definitie='De periode van de kroonontwikkeling – beheer gericht op in stand houden van de boom (onderhoudssnoei)',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGroeifase/volwassenfase')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

