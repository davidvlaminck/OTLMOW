# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSleufUitvoering(KeuzelijstField):
    """Uitvoeringen van de sleuf."""
    naam = 'KlSleufUitvoering'
    label = 'Sleuf uitvoering'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSleufUitvoering'
    definition = 'Uitvoeringen van de sleuf.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSleufUitvoering'
    options = {
        'beschoeide-sleuf': KeuzelijstWaarde(invulwaarde='beschoeide-sleuf',
                                             label='beschoeide sleuf',
                                             definitie='beschoeide sleuf',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleufUitvoering/beschoeide-sleuf'),
        'beschoeide-sleuf-met-voorafgraving': KeuzelijstWaarde(invulwaarde='beschoeide-sleuf-met-voorafgraving',
                                                               label='beschoeide sleuf met voorafgraving',
                                                               definitie='beschoeide sleuf met voorafgraving',
                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleufUitvoering/beschoeide-sleuf-met-voorafgraving'),
        'directional-drilling': KeuzelijstWaarde(invulwaarde='directional-drilling',
                                                 label='directional drilling',
                                                 definitie='directional drilling',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleufUitvoering/directional-drilling'),
        'onderdoorpersing': KeuzelijstWaarde(invulwaarde='onderdoorpersing',
                                             label='onderdoorpersing',
                                             definitie='onderdoorpersing',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleufUitvoering/onderdoorpersing'),
        'open-sleuf': KeuzelijstWaarde(invulwaarde='open-sleuf',
                                       label='open sleuf',
                                       definitie='open sleuf',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleufUitvoering/open-sleuf'),
        'waterdicht-beschoeide-sleuf-met-damplanken': KeuzelijstWaarde(invulwaarde='waterdicht-beschoeide-sleuf-met-damplanken',
                                                                       label='waterdicht beschoeide sleuf met damplanken',
                                                                       definitie='waterdicht beschoeide sleuf met damplanken',
                                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleufUitvoering/waterdicht-beschoeide-sleuf-met-damplanken')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlSleufUitvoering.get_dummy_data()

