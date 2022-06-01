# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEcoLooprichelType(KeuzelijstField):
    """Types van looprichel."""
    naam = 'KlEcoLooprichelType'
    label = 'Looprichel type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEcoLooprichelType'
    definition = 'Types van looprichel.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEcoLooprichelType'
    options = {
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  definitie='Een betonnen looprichel.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoLooprichelType/beton'),
        'doorlopende-natuurlijke-oever': KeuzelijstWaarde(invulwaarde='doorlopende-natuurlijke-oever',
                                                          label='doorlopende natuurlijke oever',
                                                          definitie='Een doorlopende natuurlijke oever.',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoLooprichelType/doorlopende-natuurlijke-oever'),
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='hout',
                                 definitie='Een houten looprichel.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoLooprichelType/hout'),
        'schanskorven': KeuzelijstWaarde(invulwaarde='schanskorven',
                                         label='schanskorven',
                                         definitie='Een oever bestaande uit schanskorven.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoLooprichelType/schanskorven')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlEcoLooprichelType.get_dummy_data()

