# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfsluiterType(KeuzelijstField):
    """De types van de afsluiter."""
    naam = 'KlAfsluiterType'
    label = 'Afsluiter type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfsluiterType'
    definition = 'De types van de afsluiter.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfsluiterType'
    options = {
        'steekschuif': KeuzelijstWaarde(invulwaarde='steekschuif',
                                        label='steekschuif',
                                        status='ingebruik',
                                        definitie='De steekschuif is een verticaal bewegend afsluitorgaan, en kan rond, vierkant of rechthoekig zijn.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfsluiterType/steekschuif'),
        'wandafsluiter': KeuzelijstWaarde(invulwaarde='wandafsluiter',
                                          label='wandafsluiter',
                                          status='ingebruik',
                                          definitie='Een afsluiter voor de beheersing van water',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfsluiterType/wandafsluiter')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlAfsluiterType.get_dummy_data()

