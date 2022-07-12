# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSelLusVerbinding(KeuzelijstField):
    """Keuzelijst met soorten verbindingen voor selectieve lussen."""
    naam = 'KlSelLusVerbinding'
    label = 'Selectieve lus verbinding'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSelLusVerbinding'
    definition = 'Keuzelijst met soorten verbindingen voor selectieve lussen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSelLusVerbinding'
    options = {
        'contact': KeuzelijstWaarde(invulwaarde='contact',
                                    label='contact',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusVerbinding/contact'),
        'serieel': KeuzelijstWaarde(invulwaarde='serieel',
                                    label='serieel',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusVerbinding/serieel')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlSelLusVerbinding.get_dummy_data()

