# coding=utf-8
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

