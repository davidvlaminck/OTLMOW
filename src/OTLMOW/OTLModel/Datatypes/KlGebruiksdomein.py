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
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGebruiksdomein'
    options = {
        'gb-gewapend': KeuzelijstWaarde(invulwaarde='gb-gewapend',
                                        label='GB (gewapend)',
                                        status='ingebruik',
                                        definitie='Gewapend beton.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruiksdomein/gb-gewapend'),
        'ob-ongewapend': KeuzelijstWaarde(invulwaarde='ob-ongewapend',
                                          label='OB (ongewapend)',
                                          status='ingebruik',
                                          definitie='Ongewapend beton.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruiksdomein/ob-ongewapend'),
        'vb-voorgespannen': KeuzelijstWaarde(invulwaarde='vb-voorgespannen',
                                             label='VB (voorgespannen)',
                                             status='ingebruik',
                                             definitie='Voorgespannen beton.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruiksdomein/vb-voorgespannen')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

