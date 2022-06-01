# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomVerankering(KeuzelijstField):
    """De verschillende manieren van verankering van een boom."""
    naam = 'KlBoomVerankering'
    label = 'Boom verankering'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomVerankering'
    definition = 'De verschillende manieren van verankering van een boom.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomVerankering'
    options = {
        'bovengronds': KeuzelijstWaarde(invulwaarde='bovengronds',
                                        label='bovengronds',
                                        definitie='De constructie voor de stabiliteit van de boom bevindt zich boven de grond',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomVerankering/bovengronds'),
        'ondergronds': KeuzelijstWaarde(invulwaarde='ondergronds',
                                        label='ondergronds',
                                        definitie='De constructie voor de stabiliteit van de boom bevindt zich volledig onder de grond',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomVerankering/ondergronds')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBoomVerankering.get_dummy_data()

