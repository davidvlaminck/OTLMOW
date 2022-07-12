# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEcoOverstaptype(KeuzelijstField):
    """Types van terugkeer voor wild."""
    naam = 'KlEcoOverstaptype'
    label = 'Overstaptype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEcoOverstaptype'
    definition = 'Types van terugkeer voor wild.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEcoOverstaptype'
    options = {
        'dassenpoort': KeuzelijstWaarde(invulwaarde='dassenpoort',
                                        label='dassenpoort',
                                        status='ingebruik',
                                        definitie='Een dassenpoortje is een luikje dat schuin in het raster bevestigd is. Dat luikje gaat maar langs één kant open en valt automatisch terug dicht.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoOverstaptype/dassenpoort'),
        'ree-overstap': KeuzelijstWaarde(invulwaarde='ree-overstap',
                                         label='ree overstap',
                                         status='ingebruik',
                                         definitie='Een verhoging aan de buitenzijde (aan de kant van de weg) met een steile afsprong naar de binnenzijde om dieren die toch aan de wegkant verzeild zijn geraakt terug naar de veilige kant te laten begeven. Door de steile afsprong kan het dier niet in de richting van de weg gaan.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoOverstaptype/ree-overstap')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlEcoOverstaptype.get_dummy_data()

