# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlExternedetectieCommunicatiewijze(KeuzelijstField):
    """Keuzelijst met de verschillende manieren waarop een externe detectie communiceert met een verkeersregelaar."""
    naam = 'KlExternedetectieCommunicatiewijze'
    label = 'Externedetectie communicatiewijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlExternedetectieCommunicatiewijze'
    definition = 'Keuzelijst met de verschillende manieren waarop een externe detectie communiceert met een verkeersregelaar.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlExternedetectieCommunicatiewijze'
    options = {
        'contact': KeuzelijstWaarde(invulwaarde='contact',
                                    label='contact',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieCommunicatiewijze/contact'),
        'protocol': KeuzelijstWaarde(invulwaarde='protocol',
                                     label='protocol',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieCommunicatiewijze/protocol'),
        'serieel': KeuzelijstWaarde(invulwaarde='serieel',
                                    label='serieel',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieCommunicatiewijze/serieel')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlExternedetectieCommunicatiewijze.get_dummy_data()

