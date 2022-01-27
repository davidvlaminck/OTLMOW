# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar(KeuzelijstField):
    """Directe of indirecte overstroombeveiliging van de vermogenschakelaar."""
    naam = 'KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar'
    label = 'HS-beveiligingscel overstroombeveiliging vermogenschakelaar'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar'
    definition = 'Directe of indirecte overstroombeveiliging van de vermogenschakelaar.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar'
    options = {
        'direct': KeuzelijstWaarde(invulwaarde='direct',
                                   label='direct',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar/direct'),
        'indirect': KeuzelijstWaarde(invulwaarde='indirect',
                                     label='indirect',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar/indirect')
    }

