# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBVBindmiddel(KeuzelijstField):
    """De mogelijke bindmiddelen bij de bitumineuze verharding."""
    naam = 'KlBVBindmiddel'
    label = 'BV bindmiddel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBVBindmiddel'
    definition = 'De mogelijke bindmiddelen bij de bitumineuze verharding.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBVBindmiddel'
    options = {
        'bindmiddel-met-additieven': KeuzelijstWaarde(invulwaarde='bindmiddel-met-additieven',
                                                      label='bindmiddel met additieven',
                                                      definitie='bindmiddel met additieven',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVBindmiddel/bindmiddel-met-additieven'),
        'bindmiddel-met-positief-indringingsgetal': KeuzelijstWaarde(invulwaarde='bindmiddel-met-positief-indringingsgetal',
                                                                     label='bindmiddel met positief indringingsgetal',
                                                                     definitie='bindmiddel met positief indringingsgetal',
                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVBindmiddel/bindmiddel-met-positief-indringingsgetal'),
        'gewoon-wegenbitumen': KeuzelijstWaarde(invulwaarde='gewoon-wegenbitumen',
                                                label='gewoon wegenbitumen',
                                                definitie='gewoon wegenbitumen',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVBindmiddel/gewoon-wegenbitumen'),
        'gewoon-wegenbitumen-met-natuurbitumen': KeuzelijstWaarde(invulwaarde='gewoon-wegenbitumen-met-natuurbitumen',
                                                                  label='gewoon wegenbitumen met natuurbitumen',
                                                                  definitie='gewoon wegenbitumen met natuurbitumen',
                                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVBindmiddel/gewoon-wegenbitumen-met-natuurbitumen'),
        'hard-bitumen-B-10-20-of-B15-25': KeuzelijstWaarde(invulwaarde='hard-bitumen-B-10-20-of-B15-25',
                                                           label='hard bitumen B 10-20 of B15-25',
                                                           definitie='hard bitumen B 10/20 of B15/25',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVBindmiddel/hard-bitumen-B-10-20-of-B15-25'),
        'kleurloos-synthetisch-bindmiddel': KeuzelijstWaarde(invulwaarde='kleurloos-synthetisch-bindmiddel',
                                                             label='kleurloos synthetisch bindmiddel',
                                                             definitie='kleurloos synthetisch bindmiddel',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVBindmiddel/kleurloos-synthetisch-bindmiddel'),
        'met-polymeren-gemodificeerd-kleurloos-synthetisch-bindmiddel': KeuzelijstWaarde(invulwaarde='met-polymeren-gemodificeerd-kleurloos-synthetisch-bindmiddel',
                                                                                         label='met polymeren gemodificeerd kleurloos synthetisch bindmiddel',
                                                                                         definitie='met polymeren gemodificeerd kleurloos synthetisch bindmiddel',
                                                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVBindmiddel/met-polymeren-gemodificeerd-kleurloos-synthetisch-bindmiddel'),
        'niet-gespecifieerd-(keuze-van-de-aannemer)': KeuzelijstWaarde(invulwaarde='niet-gespecifieerd-(keuze-van-de-aannemer)',
                                                                       label='niet gespecifieerd (keuze van de aannemer)',
                                                                       definitie='niet gespecifieerd (keuze van de aannemer)',
                                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVBindmiddel/niet-gespecifieerd-(keuze-van-de-aannemer)'),
        'pigmenteerbaar-bitumen': KeuzelijstWaarde(invulwaarde='pigmenteerbaar-bitumen',
                                                   label='pigmenteerbaar bitumen',
                                                   definitie='pigmenteerbaar bitumen',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVBindmiddel/pigmenteerbaar-bitumen'),
        'polymeerbitumen': KeuzelijstWaarde(invulwaarde='polymeerbitumen',
                                            label='polymeerbitumen',
                                            definitie='polymeerbitumen',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBVBindmiddel/polymeerbitumen')
    }

