# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar(KeuzelijstField):
    """Directe of indirecte overstroombeveiliging van de vermogenschakelaar."""
    naam = 'KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar'
    label = 'HS-beveiligingscel overstroombeveiliging vermogenschakelaar'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar'
    definition = 'Directe of indirecte overstroombeveiliging van de vermogenschakelaar.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar'
    options = {
        'direct': KeuzelijstWaarde(invulwaarde='direct',
                                   label='direct',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar/direct'),
        'indirect': KeuzelijstWaarde(invulwaarde='indirect',
                                     label='indirect',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar/indirect')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

