# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSeinbrugRijrichting(KeuzelijstField):
    """Mogelijke rijrichtingen bij een seinbrug (enkele of dubbele)."""
    naam = 'KlSeinbrugRijrichting'
    label = 'Seinbrug rijrichting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSeinbrugRijrichting'
    definition = 'Mogelijke rijrichtingen bij een seinbrug (enkele of dubbele).'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSeinbrugRijrichting'
    options = {
        'dubbele-rijrichting': KeuzelijstWaarde(invulwaarde='dubbele-rijrichting',
                                                label='dubbele rijrichting',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinbrugRijrichting/dubbele-rijrichting'),
        'enkele-rijrichting': KeuzelijstWaarde(invulwaarde='enkele-rijrichting',
                                               label='enkele rijrichting',
                                               status='ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinbrugRijrichting/enkele-rijrichting')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlSeinbrugRijrichting.get_dummy_data()

