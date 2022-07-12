# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAardingAardingsstelsel(KeuzelijstField):
    """Lijst van mogelijke aardinggsstelsels."""
    naam = 'KlAardingAardingsstelsel'
    label = 'Aardingsinstallatie aardingsstelsel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlAardingAardingsstelsel'
    definition = 'Lijst van mogelijke aardinggsstelsels.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAardingAardingsstelsel'
    options = {
        'gemeenschappelijk': KeuzelijstWaarde(invulwaarde='gemeenschappelijk',
                                              label='gemeenschappelijk',
                                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                              definitie='Een aardingsstelsel waarin de aardingen (LS, N, HS) met elkaar verbonden zijn. Indien de distributienetbeheerder met een attest garandeerd dat de aardingen verbonden zijn met andere aardingsinstallaties is er sprake van een gemeenschappelijk globaal stelsel en moet die optie gekozen worden.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingAardingsstelsel/gemeenschappelijk'),
        'gemeenschappelijk---globaal': KeuzelijstWaarde(invulwaarde='gemeenschappelijk---globaal',
                                                        label='gemeenschappelijk + globaal',
                                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                        definitie='Een aardingsstelsel waarin alle aardingen (LS, N, HS) met elkaar verbonden zijn en waarvoor bovendien de distributienetbeheerder aan de hand van een attest garandeert dat de aardingen verbonden zijn met ten minste x andere aardingsinstallaties van andere installaties. Voor een globaal stelsel moet altijd het attest toegevoegd worden. Zonder dergelijk attest kan er enkel sprake zijn van een gemeenschappelijk stelsel en moet die optie gekozen worden.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingAardingsstelsel/gemeenschappelijk---globaal'),
        'gescheiden': KeuzelijstWaarde(invulwaarde='gescheiden',
                                       label='gescheiden',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Een aardingsstelsel waarin de aardingen (LS, N, HS) niet met elkaar verbonden zijn.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingAardingsstelsel/gescheiden')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlAardingAardingsstelsel.get_dummy_data()

