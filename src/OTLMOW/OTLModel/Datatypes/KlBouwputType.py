# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBouwputType(KeuzelijstField):
    """Het type van bouwput."""
    naam = 'KlBouwputType'
    label = 'Bouwput type.'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBouwputType'
    definition = 'Het type van bouwput.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBouwputType'
    options = {
        'bouwput': KeuzelijstWaarde(invulwaarde='bouwput',
                                    label='bouwput',
                                    status='ingebruik',
                                    definitie='bouwput',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBouwputType/bouwput'),
        'intredeput': KeuzelijstWaarde(invulwaarde='intredeput',
                                       label='intredeput',
                                       status='ingebruik',
                                       definitie='intredeput',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBouwputType/intredeput'),
        'ontvangstput': KeuzelijstWaarde(invulwaarde='ontvangstput',
                                         label='ontvangstput',
                                         status='ingebruik',
                                         definitie='ontvangstput',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBouwputType/ontvangstput'),
        'persput': KeuzelijstWaarde(invulwaarde='persput',
                                    label='persput',
                                    status='ingebruik',
                                    definitie='persput',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBouwputType/persput')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBouwputType.get_dummy_data()

