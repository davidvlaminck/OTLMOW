# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOmvormerType(KeuzelijstField):
    """De soort omvorming die gebeurt er in de omvormer."""
    naam = 'KlOmvormerType'
    label = 'Omvormer type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOmvormerType'
    definition = 'De soort omvorming die gebeurt er in de omvormer.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOmvormerType'
    options = {
        'Coax-UTP': KeuzelijstWaarde(invulwaarde='Coax-UTP',
                                     label='Coax-UTP',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/Coax-UTP'),
        'Decoder': KeuzelijstWaarde(invulwaarde='Decoder',
                                    label='Decoder',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/Decoder'),
        'Encoder': KeuzelijstWaarde(invulwaarde='Encoder',
                                    label='Encoder',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/Encoder'),
        'Glasvezel-UTP': KeuzelijstWaarde(invulwaarde='Glasvezel-UTP',
                                          label='Glasvezel-UTP',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/Glasvezel-UTP'),
        'UTP-(Serieel)-UTP': KeuzelijstWaarde(invulwaarde='UTP-(Serieel)-UTP',
                                              label='UTP (Serieel)-UTP',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/UTP-(Serieel)-UTP'),
        'UTP-Coax': KeuzelijstWaarde(invulwaarde='UTP-Coax',
                                     label='UTP-Coax',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/UTP-Coax'),
        'UTP-Glasvezel': KeuzelijstWaarde(invulwaarde='UTP-Glasvezel',
                                          label='UTP-Glasvezel',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/UTP-Glasvezel'),
        'UTP-UTP-(serieel)': KeuzelijstWaarde(invulwaarde='UTP-UTP-(serieel)',
                                              label='UTP-UTP (serieel)',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/UTP-UTP-(serieel)'),
        'draadloos-utp': KeuzelijstWaarde(invulwaarde='draadloos-utp',
                                          label='Draadloos-UTP',
                                          definitie='Draadloos-UTP',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/draadloos-utp'),
        'utp-draadloos': KeuzelijstWaarde(invulwaarde='utp-draadloos',
                                          label='UTP-Draadloos',
                                          definitie='UTP-Draadloos',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/utp-draadloos')
    }

