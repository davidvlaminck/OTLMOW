# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPlaatsingswijzePlint(KeuzelijstField):
    """De manier waarop de plint geplaatst is ten opzichte van de profielen."""
    naam = 'KlPlaatsingswijzePlint'
    label = 'Plaatsingswijze plint'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPlaatsingswijzePlint'
    definition = 'De manier waarop de plint geplaatst is ten opzichte van de profielen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPlaatsingswijzePlint'
    options = {
        'bevestigd-tegen-de-profielen': KeuzelijstWaarde(invulwaarde='bevestigd-tegen-de-profielen',
                                                         label='bevestigd tegen de profielen',
                                                         definitie='bevestigd tegen de profielen',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlaatsingswijzePlint/bevestigd-tegen-de-profielen'),
        'geschoven-tussen-de-profielen': KeuzelijstWaarde(invulwaarde='geschoven-tussen-de-profielen',
                                                          label='geschoven tussen de profielen',
                                                          definitie='geschoven tussen de profielen',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlaatsingswijzePlint/geschoven-tussen-de-profielen')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlPlaatsingswijzePlint.get_dummy_data()

