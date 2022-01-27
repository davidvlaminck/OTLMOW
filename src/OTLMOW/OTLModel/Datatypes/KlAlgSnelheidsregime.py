# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgSnelheidsregime(KeuzelijstField):
    """De snelheidsregimes met variabele mogelijkeid."""
    naam = 'KlAlgSnelheidsregime'
    label = 'Snelheidsregime'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAlgSnelheidsregime'
    definition = 'De snelheidsregimes met variabele mogelijkeid.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgSnelheidsregime'
    options = {
        '120': KeuzelijstWaarde(invulwaarde='120',
                                label='120',
                                definitie='120 km/h.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/120'),
        '30': KeuzelijstWaarde(invulwaarde='30',
                               label='30',
                               definitie='30 km/h.',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/30'),
        '50': KeuzelijstWaarde(invulwaarde='50',
                               label='50',
                               definitie='50 km/h.',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/50'),
        '60': KeuzelijstWaarde(invulwaarde='60',
                               label='60',
                               definitie='60 km/h.',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/60'),
        '70': KeuzelijstWaarde(invulwaarde='70',
                               label='70',
                               definitie='70 km/h.',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/70'),
        '80': KeuzelijstWaarde(invulwaarde='80',
                               label='80',
                               definitie='80 km/h.',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/80'),
        '90': KeuzelijstWaarde(invulwaarde='90',
                               label='90',
                               definitie='90 km/h.',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/90'),
        'variabel': KeuzelijstWaarde(invulwaarde='variabel',
                                     label='variabel',
                                     definitie='Variabele ingave.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgSnelheidsregime/variabel')
    }

