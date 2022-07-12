# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOmvormerType(KeuzelijstField):
    """De soort omvorming die gebeurt er in de omvormer."""
    naam = 'KlOmvormerType'
    label = 'Omvormer type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOmvormerType'
    definition = 'De soort omvorming die gebeurt er in de omvormer.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOmvormerType'
    options = {
        'Coax-UTP': KeuzelijstWaarde(invulwaarde='Coax-UTP',
                                     label='Coax-UTP',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/Coax-UTP'),
        'Decoder': KeuzelijstWaarde(invulwaarde='Decoder',
                                    label='Decoder',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/Decoder'),
        'Encoder': KeuzelijstWaarde(invulwaarde='Encoder',
                                    label='Encoder',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/Encoder'),
        'Glasvezel-UTP': KeuzelijstWaarde(invulwaarde='Glasvezel-UTP',
                                          label='Glasvezel-UTP',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/Glasvezel-UTP'),
        'UTP-(Serieel)-UTP': KeuzelijstWaarde(invulwaarde='UTP-(Serieel)-UTP',
                                              label='UTP (Serieel)-UTP',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/UTP-(Serieel)-UTP'),
        'UTP-Coax': KeuzelijstWaarde(invulwaarde='UTP-Coax',
                                     label='UTP-Coax',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/UTP-Coax'),
        'UTP-Glasvezel': KeuzelijstWaarde(invulwaarde='UTP-Glasvezel',
                                          label='UTP-Glasvezel',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/UTP-Glasvezel'),
        'UTP-UTP-(serieel)': KeuzelijstWaarde(invulwaarde='UTP-UTP-(serieel)',
                                              label='UTP-UTP (serieel)',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/UTP-UTP-(serieel)'),
        'draadloos-utp': KeuzelijstWaarde(invulwaarde='draadloos-utp',
                                          label='Draadloos-UTP',
                                          status='ingebruik',
                                          definitie='Draadloos-UTP',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/draadloos-utp'),
        'utp-draadloos': KeuzelijstWaarde(invulwaarde='utp-draadloos',
                                          label='UTP-Draadloos',
                                          status='ingebruik',
                                          definitie='UTP-Draadloos',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/utp-draadloos')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlOmvormerType.get_dummy_data()

