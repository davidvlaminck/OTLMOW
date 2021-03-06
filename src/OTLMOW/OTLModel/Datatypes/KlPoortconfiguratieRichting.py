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
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPoortconfiguratieRichting'
    options = {
        'ingaand': KeuzelijstWaarde(invulwaarde='ingaand',
                                    label='ingaand',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPoortconfiguratieRichting/ingaand'),
        'uitgaand': KeuzelijstWaarde(invulwaarde='uitgaand',
                                     label='uitgaand',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPoortconfiguratieRichting/uitgaand')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

