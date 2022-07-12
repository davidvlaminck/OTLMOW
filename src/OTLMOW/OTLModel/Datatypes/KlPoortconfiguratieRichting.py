# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPoortconfiguratieRichting(KeuzelijstField):
    """De richting waarin de poort openstaat."""
    naam = 'KlPoortconfiguratieRichting'
    label = 'Poortconfiguratie richting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPoortconfiguratieRichting'
    definition = 'De richting waarin de poort openstaat.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPoortconfiguratieRichting'
    options = {
        'ingaand': KeuzelijstWaarde(invulwaarde='ingaand',
                                    label='ingaand',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPoortconfiguratieRichting/ingaand'),
        'uitgaand': KeuzelijstWaarde(invulwaarde='uitgaand',
                                     label='uitgaand',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPoortconfiguratieRichting/uitgaand')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlPoortconfiguratieRichting.get_dummy_data()

