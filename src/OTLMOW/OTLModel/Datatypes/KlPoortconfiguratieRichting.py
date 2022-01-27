# coding=utf-8
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
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPoortconfiguratieRichting/ingaand'),
        'uitgaand': KeuzelijstWaarde(invulwaarde='uitgaand',
                                     label='uitgaand',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPoortconfiguratieRichting/uitgaand')
    }

