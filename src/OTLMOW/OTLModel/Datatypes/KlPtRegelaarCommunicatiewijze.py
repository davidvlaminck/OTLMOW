# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPtRegelaarCommunicatiewijze(KeuzelijstField):
    """Keuzelijst met de verschillende manieren waarop een PT_Regelaar communiceert met de Verkeersregelaar."""
    naam = 'KlPtRegelaarCommunicatiewijze'
    label = 'Ptregelaar communicatiewijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPtRegelaarCommunicatiewijze'
    definition = 'Keuzelijst met de verschillende manieren waarop een PT_Regelaar communiceert met de Verkeersregelaar.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPtRegelaarCommunicatiewijze'
    options = {
        'VR-PT-kaart': KeuzelijstWaarde(invulwaarde='VR-PT-kaart',
                                        label='VR PT-kaart',
                                        definitie='De PT kaart is een module die is ingebouwd in de verkeersregelaar',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPtRegelaarCommunicatiewijze/VR-PT-kaart'),
        'contact': KeuzelijstWaarde(invulwaarde='contact',
                                    label='contact',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPtRegelaarCommunicatiewijze/contact'),
        'protocol': KeuzelijstWaarde(invulwaarde='protocol',
                                     label='protocol',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPtRegelaarCommunicatiewijze/protocol'),
        'serieel': KeuzelijstWaarde(invulwaarde='serieel',
                                    label='serieel',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPtRegelaarCommunicatiewijze/serieel')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlPtRegelaarCommunicatiewijze.get_dummy_data()

