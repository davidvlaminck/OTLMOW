# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGebruiksdomein(KeuzelijstField):
    """De omstandigheden waarin het beton gebruikt zal worden."""
    naam = 'KlGebruiksdomein'
    label = 'Gebruiksdomein'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlGebruiksdomein'
    definition = 'De omstandigheden waarin het beton gebruikt zal worden.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGebruiksdomein'
    options = {
        'gb-gewapend': KeuzelijstWaarde(invulwaarde='gb-gewapend',
                                        label='GB (gewapend)',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='Gewapend beton.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruiksdomein/gb-gewapend'),
        'ob-ongewapend': KeuzelijstWaarde(invulwaarde='ob-ongewapend',
                                          label='OB (ongewapend)',
                                          status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='Ongewapend beton.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruiksdomein/ob-ongewapend'),
        'vb-voorgespannen': KeuzelijstWaarde(invulwaarde='vb-voorgespannen',
                                             label='VB (voorgespannen)',
                                             status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                             definitie='Voorgespannen beton.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruiksdomein/vb-voorgespannen')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlGebruiksdomein.get_dummy_data()

